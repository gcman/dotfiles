#!/usr/bin/env python3
from os import environ

def send_command_to_qute(command):
    with open(environ.get("QUTE_FIFO"), "w") as f:
        f.write(command)        

command = "open javascript:location.href='org-protocol://capture-html?template=p&url=' + encodeURIComponent(location.href) + '&title=' + encodeURIComponent(document.title || '[untitled page]') + '&body=' + encodeURIComponent(function () {var html = ''; if (typeof document.getSelection != 'undefined') {var sel = document.getSelection(); if (sel.rangeCount) {var container = document.createElement('div'); for (var i = 0, len = sel.rangeCount; i < len; ++i) {container.appendChild(sel.getRangeAt(i).cloneContents());} html = container.innerHTML;}} else if (typeof document.selection != 'undefined') {if (document.selection.type == 'Text') {html = document.selection.createRange().htmlText;}} var relToAbs = function (href) {var a = document.createElement('a'); a.href = href; var abs = a.protocol + '//' + a.host + a.pathname + a.search + a.hash; a.remove(); return abs;}; var elementTypes = [['a', 'href'], ['img', 'src']]; var div = document.createElement('div'); div.innerHTML = html; elementTypes.map(function(elementType) {var elements = div.getElementsByTagName(elementType[0]); for (var i = 0; i < elements.length; i++) {elements[i].setAttribute(elementType[1], relToAbs(elements[i].getAttribute(elementType[1])));}}); return div.innerHTML;}());"

if ".pdf" in environ.get("QUTE_URL"):
    send_command_to_qute("spawn emacsclient org-protocol://capture?template=q&title={title}")
else:
    if environ.get("QUTE_SELECTED_TEXT"):
        send_command_to_qute(command)
    else:
        send_command_to_qute("spawn emacsclient org-protocol://capture?template=p&title={title}&url={url}&body=''")
