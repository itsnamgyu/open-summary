function summarizeArticle() {
    const $url = $("#summarize-button").data('summarize-url');

    const $summaryProgress = $("#summary-progress");
    const $summaryDone = $("#summary-done");
    const $summaryError = $("#summary-error");

    $summaryProgress.fadeIn();
    $.ajax({
        url: $url,
        method: 'POST',
        success: function (data) {
            $summaryProgress.fadeOut(200, function () {
                $summaryDone.fadeIn();
            });
            setTimeout(function () {
                window.location.reload();
            }, 1000);
        },
        error: function () {
            setTimeout(function () {
                $summaryProgress.fadeOut(200, function () {
                    $summaryError.fadeIn(200);
                });
            }, 2000);
        }
    });
}

function parseAndSummarizeArticle() {
    const $url = $("#summarize-button").data('parse-url');
    $("#summarize-button").attr('disabled', true);

    const $parseProgress = $("#parse-progress");
    const $parseDone = $("#parse-done");
    const $parseError = $("#parse-error");

    $parseProgress.fadeIn();
    $.ajax({
        url: $url,
        method: 'POST',
        success: function (data) {
            $parseProgress.fadeOut(200, function () {
                $parseDone.fadeIn(200, function () {
                    summarizeArticle();
                })
            });
        },
        error: function () {
            setTimeout(function () {
                $parseProgress.fadeOut(200, function () {
                    $parseError.fadeIn(200);
                });
            }, 2000);
        }
    });
}

$(function () {
    const $shareButton = $("#share-button");
    $shareButton.click(function () {
        navigator.share({
            text: 'OpenSummary - ' + $shareButton.data('title'),
            url: $shareButton.data('url'),
        }).then(() => {
        });
    });

    const $summarizeButton = $("#summarize-button");
    $summarizeButton.click(function () {
        parseAndSummarizeArticle();
    });

    const $resetSummaryButton = $("#reset-summary-button");
    $resetSummaryButton.click(function () {
        const $url = $resetSummaryButton.data('reset-summary-url');
        $.ajax({
            url: $url,
            method: 'POST',
            success: function (data) {
                window.location.reload();
            },
        });
    });
});