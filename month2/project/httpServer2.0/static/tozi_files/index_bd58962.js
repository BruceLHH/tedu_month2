$(document).ready(function(){function i(){n(),s()}function n(){e=window.Thunder.create({baseParams:{ct:2,logFrom:"recdetail",logid:window.s_session.logid||"0",ssid:window.s_session.ssid||"0",sid:window.s_session.sid||"0",qid:window.s_session.qid||"0"}})}function s(){e.send({tid:10814,cst:1,logInfo:"show",logExtra:JSON.stringify([{rid:window.s_session.nid||"0"}]),r:window.s_session.timestamp||"0"})}F.call("superlanding:article/usrMenu","init"),F.call("superlanding:article/topBtm","init"),F.call("superlanding:article/log","init"),F.call("superlanding:article/richText","init"),F.call("superlanding:article/video","init"),F.call("superlanding:article/music","init"),F.call("superlanding:article/qrcode","init");var e;i(),$(".error-wrapper").length>0&&$("#goback").on("click",function(){history.go(-1)}),$.ajax({url:"https://mbd.baidu.com/newspage/api/getusername",type:"get",dataType:"jsonp",jsonp:"cb",success:function(i){var n=$("#userBlock"),s="";i&&i.username?(s="login",$("#nametxt").html(i.username)):s="unlogin",n.addClass(s).css("display","inline-block")}});var a=navigator.userAgent.toLowerCase();if(-1===a.indexOf("applewebkit")&&$(".related-news").length>0){var l=$(".related-news").find("a");l.hasClass("upgrade")&&l.removeClass("upgrade").addClass("degrade")}});