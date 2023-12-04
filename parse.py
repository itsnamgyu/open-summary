from typing import Dict

import requests
import re

URL = 'http://127.0.0.1:8503/predict'
SECTION_BREAK = (
    "References", "references", "Acknowledgements", "ackno", "Limitations", "limitations", 'Acknowledgement',
    'acknowledgement')


def nougat_request(file_path: str):
    pdf_file = file_path.split('/')[-1]

    url = URL
    headers = {'accept': 'application/json'}
    files = {'file': (f'{pdf_file}', open(f'{file_path}', 'rb'), 'application/pdf')}

    response = requests.post(url, headers=headers, files=files)

    return response.content


def extract_between_markers(context):
    # Use a regular expression to find all occurrences of sections starting with "\n## "
    pattern = r'(?<=\n## )(.*?)(?=\n## |$)'
    sections = re.findall(pattern, context, re.DOTALL)

    # Prepend "\n## " to each section, except the first one if it was originally not following "\n## "
    for i in range(len(sections)):
        sections[i] = '##' + sections[i]

    return sections


def extract_section_name(context):
    # Use a regular expression to find the first text between "##" and "\n"
    match = re.search(r'##(.*?)(?=\n)', context, re.DOTALL)

    # If a match is found, return it; otherwise, return an empty string or a message
    return match.group(1).strip() if match else ""


def extract_section_content(context):
    # Find the position of the first newline character
    newline_pos = context.find('\n')

    # Extract everything after the first newline
    return context[newline_pos + 1:] if newline_pos != -1 else context


def remove_tables(context):
    # Use a regular expression to remove everything between \begin{table} and \end{table} including the markers
    cleaned_context = re.sub(r'\\begin\{table\}.*?\\end\{table\}', '', context, flags=re.DOTALL)

    return cleaned_context


def remove_tabular(context):
    # Use a regular expression to remove everything between \begin{table} and \end{table} including the markers
    cleaned_context = re.sub(r'\\begin\{tabular\}.*?\n', '', context, flags=re.DOTALL)

    return cleaned_context


def remove_table_caption(text):
    # Use a regular expression to remove everything between \begin{table} and \end{table} including the markers
    cleaned_text = re.sub(r'\nTable.*?\n', '', text, flags=re.DOTALL)
    return cleaned_text


def remove_figure_caption(text):
    # Use a regular expression to remove everything between \begin{table} and \end{table} including the markers
    cleaned_text = re.sub(r'\nFigure.*?\n', '', text, flags=re.DOTALL)

    return cleaned_text


def remove_footnote(text):
    # Use a regular expression to remove everything between "\nFootnote" and the next "\n", including "\nFootnote"
    cleaned_text = re.sub(r'\nFootnote.*?\n', '', text, flags=re.DOTALL)

    return cleaned_text


def remove_code_block(text):
    # Use a regular expression to remove everything between triple backticks, including the backticks
    cleaned_text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)

    return cleaned_text


def extract_abstract(context):
    # Define the start and end markers
    start_marker = "###### Abstract"
    end_marker = "\n\n##"

    # Find the start and end positions
    start_pos = context.find(start_marker)
    end_pos = context.find(end_marker, start_pos)

    # Extract and return the text between the markers
    if start_pos != -1 and end_pos != -1:
        # Adjust start position to account for the length of the start marker
        start_pos += len(start_marker)
        return context[start_pos:end_pos].strip()
    else:
        return None


def extract_title(context):
    # Find the position of the first newline character
    end_pos = context.find('\n')
    # Extract the text before the first newline
    title = context[:end_pos] if end_pos != -1 else context
    title = re.sub(r'# ', '', title, flags=re.DOTALL)
    title = title.rstrip()
    title = title.lstrip()
    return title


def preprocessing(text):
    section_content = remove_tables(text)
    section_content = remove_tabular(section_content)
    section_content = remove_table_caption(section_content)
    section_content = remove_figure_caption(section_content)
    section_content = remove_footnote(section_content)
    section_content = remove_code_block(section_content)
    return section_content


def split_sections(content, pdf_file, agg_split=True):
    template = {'file': pdf_file}

    decode_object = content.decode('utf-8')
    formatted_string = decode_object.replace('\\n', '\n')
    formatted_string = formatted_string[1:-1]

    title = extract_title(formatted_string)
    abstract = extract_abstract(formatted_string)

    template['title'] = title
    if abstract:
        abstract += '\n'
        abstract = preprocessing(abstract)
        template['abstract'] = abstract
    else:
        template['abstract'] = ''

    template['sections'] = []
    sections = extract_between_markers(formatted_string)

    for sec in sections:
        section_name = extract_section_name(sec)
        flag = 0
        for section_breaker in SECTION_BREAK:
            if section_breaker.lower() in section_name.lower():
                flag = 1
        if flag == 1:
            break

        section_content = extract_section_content(sec)
        section_content = preprocessing(section_content)
        section_template = {
            section_name: section_content
        }

        template['sections'].append(section_template)

    if agg_split:
        integrated_and_split_sections = []

        temp_key = []
        temp_val = ''
        for sec in template['sections']:

            for key, value in sec.items():
                if len(value) >= 10000:
                    # temp = value.split()
                    num_splits = len(value) // 10000

                    for i, ind in enumerate(range(0, len(value), 10000)):
                        integrated_and_split_sections.append({f'{key}-{i + 1}': value[ind:ind + 10000]})

                elif len(value) <= 2000:
                    temp_key.append(key)
                    temp_val += f'Section: {key}\n{value}\n'

                    if len(value) > 3000:
                        integrated_and_split_sections.append({' - '.join(temp_key): temp_val})
                        temp_key = []
                        temp_val = ''

                else:
                    integrated_and_split_sections.append({key: value})

        if len(temp_val):
            integrated_and_split_sections.append({'-'.join(temp_key): temp_val})

        template['sections'] = integrated_and_split_sections

    return template


def parse(path: str) -> Dict:
    """

    :param path:
    :return: {
        'file': 'filename.pdf',
        'title': 'Title of the paper',
        'abstract': 'Abstract of the paper',
        'sections': [
            {
                'section_name': 'section_content'
            },
            ...
        ],
    }
    """
    content = nougat_request(path)
    template = split_sections(content, path, agg_split=True)
    return template
