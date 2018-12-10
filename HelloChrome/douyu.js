chrome.runtime.onMessage.addListener(//监听扩展程序进程或内容脚本发送请求的请求
    function (request, sender, sendResponse) {
        if (request.action == "send") {
            console.log(request.keyword);
            console.log(request.super_link);
            var super_css = $('#js-player-asideMain div.BarrageSuperLinkPop');
            super_css.css('display','block'); 
            var super_link = $('#js-player-asideMain div.BarrageSuperLinkPop-from > textarea.BarrageSuperLinkPop-area');
            super_link.val(request.super_link);
            var danmu_cont = $('#js-player-asideMain div.ChatSend > textarea.ChatSend-txt');
            danmu_cont.val(request.keyword);
            console.log(danmu_cont);
            console.log(super_link);
            sendResponse({state:'关键词填写成功！'});
        }
        if (request.action == "submit") {
            var b_btn = $('#js-player-asideMain div.ChatSend > .ChatSend-button');
            b_btn.click();
            sendResponse({state:'提交成功！'})
            var super_css = $('#js-player-asideMain div.BarrageSuperLinkPop');
            super_css.css('display','none'); 
        }
    }
);
