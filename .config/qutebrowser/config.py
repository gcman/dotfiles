# Unbind some standard qutebrowser bindings
c.bindings.default = {}
# If you don't want to unbind everything it might be necessary to
# unbind at least the conflicting keybindings like this:

def bind_chained(key, *commands):
    config.bind(key, ' ;; '.join(commands))
    
# Reload config
config.bind('<Ctrl-x><Ctrl-l>', 'config-source')

config.bind('<Ctrl-E>', 'open-editor', mode='insert')
c.editor.command = ['emacsclient', '-c', '{}']

config.bind('<', 'scroll-to-perc 0')
config.bind('>', 'scroll-to-perc')
config.bind('<Ctrl-n>', 'scroll down')
config.bind('<Ctrl-p>', 'scroll up')
config.bind('j', 'scroll down')
config.bind('k', 'scroll up')
config.bind('<Ctrl-a>', 'back')
config.bind('<Ctrl-e>', 'forward')
config.bind('<Ctrl-x><Ctrl-f>', 'set-cmd-text -s :open -t')
config.bind('<Ctrl-u><Ctrl-x><Ctrl-f>', 'set-cmd-text -s :open')
config.bind('<Alt-w>', 'yank selection')
config.bind('yu', 'yank url')
config.bind('yf', 'set-cmd-text :open {url}')
config.bind('<Ctrl-y>', 'insert-text', mode='insert')
config.bind('<Ctrl-y>', 'insert-text', mode='command')

config.bind('f', 'set-cmd-text -s :open -t')
config.bind('F', 'set-cmd-text -s :open')

config.bind('<Escape>', 'leave-mode', mode='insert')
config.bind('<Ctrl-g>', 'leave-mode', mode='insert')
config.bind('<Ctrl-m>', 'enter-mode insert')

# emacs like bindings
config.bind('<ctrl-h>', 'fake-key <backspace>', mode='insert')
config.bind('<ctrl-d>', 'fake-key <delete>', mode='insert')
config.bind('<ctrl-f>', 'fake-key <right>', mode='insert')
config.bind('<ctrl-b>', 'fake-key <left>', mode='insert')

# close qutebrowser
config.bind('<Ctrl-x><Ctrl-c>', 'quit') # warning: closes all windows

# tab management
config.bind('<Ctrl-x>0', 'tab-close')
config.bind('<Ctrl-x>k', 'tab-close')
config.bind('d', 'tab-close')
config.bind('D', 'tab-clone')
config.bind('u', 'undo')
config.bind('<Ctrl-x>1', 'tab-only')
config.bind('<Alt-a>', 'tab-prev')
config.bind('<Alt-e>', 'tab-next')
config.bind('p', 'tab-prev')
config.bind('n', 'tab-next')
config.bind('<Ctrl-x>l', 'reload')
config.bind('r', 'reload')

# Searching
config.bind('s', 'set-cmd-text /', mode='normal')
config.bind('/', 'set-cmd-text /', mode='normal')
config.bind('?', 'set-cmd-text ?', mode='normal')
config.bind('<Ctrl-s>', 'set-cmd-text /', mode='normal')
config.bind('<Ctrl-r>', 'set-cmd-text ?', mode='normal')
config.bind('<Ctrl-s>', 'search-next', mode='command')
config.bind('<Ctrl-r>', 'search-prev', mode='command')

## Bindings for caret mode
config.bind('g', 'enter-mode caret')
config.bind('g', 'leave-mode', mode='caret')
config.bind('<Escape>', 'leave-mode', mode='caret')
config.bind('<Ctrl-g>', 'leave-mode', mode='caret')
config.bind('<Ctrl-t>', 'toggle-selection', mode='caret')
config.bind('w', 'yank selection', mode='caret')
config.bind('W', 'move-to-start-of-document ;; toggle-selection ;; move-to-end-of-document ;; yank selection', mode='caret')
config.bind('<Alt-w>', 'yank selection', mode='caret')
config.bind('<Ctrl-a>', 'move-to-end-of-line', mode='caret')
config.bind('<Ctrl-e>', 'move-to-start-of-line', mode='caret')
config.bind('<Ctrl-Space>', 'drop-selection', mode='caret')
config.bind('<Escape>', 'leave-mode', mode='caret')
config.bind('<Ctrl-b>', 'move-to-prev-char', mode='caret')
config.bind('<Ctrl-n>', 'move-to-next-line', mode='caret')
config.bind('<Ctrl-p>', 'move-to-prev-line', mode='caret')
config.bind('<Ctrl-f>', 'move-to-next-char', mode='caret')
config.bind('<Alt-f>', 'move-to-next-word', mode='caret')
config.bind('h', 'scroll left', mode='caret')
config.bind('j', 'scroll down', mode='caret')
config.bind('k', 'scroll up', mode='caret')
config.bind('l', 'scroll right', mode='caret')

config.bind('G', 'move-to-end-of-document', mode='caret')
config.bind('Y', 'yank selection -s', mode='caret')
config.bind('[', 'move-to-start-of-prev-block', mode='caret')
config.bind(']', 'move-to-start-of-next-block', mode='caret')
config.bind('b', 'move-to-prev-word', mode='caret')
config.bind('c', 'enter-mode normal', mode='caret')
config.bind('e', 'move-to-end-of-word', mode='caret')
config.bind('gg', 'move-to-start-of-document', mode='caret')
config.bind('y', 'yank selection', mode='caret')
config.bind('{', 'move-to-end-of-prev-block', mode='caret')
config.bind('}', 'move-to-end-of-next-block', mode='caret')


# zooming
config.bind('+', 'zoom-in')
config.bind('-', 'zoom-out')

# command mode
config.bind('<Ctrl-Space>', 'set-cmd-text :')
config.bind('<Alt-x>', 'set-cmd-text :')
config.bind(':', 'set-cmd-text :')
config.bind('<Up>', 'command-history-prev', mode='command')
config.bind('<Alt-p>', 'command-history-prev', mode='command')
config.bind('<Down>', 'command-history-next', mode='command')
config.bind('<Alt-n>', 'command-history-next', mode='command')
config.bind('<Escape>', 'leave-mode', mode='command')
config.bind('<Ctrl-g>', 'leave-mode', mode='command')
config.bind('<Return>', 'command-accept', mode='command')
config.bind('<Ctrl-m>', 'command-accept', mode='command')
config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
config.bind('<Ctrl-Shift-i>', 'completion-item-focus prev', mode='command')
config.bind('<Ctrl-p>', 'completion-item-focus prev', mode='command')
config.bind('<Tab>', 'completion-item-focus next', mode='command')
config.bind('<Ctrl-i>', 'completion-item-focus next', mode='command')
config.bind('<Ctrl-n>', 'completion-item-focus next', mode='command')
config.bind('<Alt-b>', 'rl-backward-word', mode='command')
config.bind('<Ctrl-w>', 'rl-backward-kill-word', mode='command')
config.bind('<Alt-d>', 'rl-kill-word', mode='command')
config.bind('<Alt-f>', 'rl-forward-word', mode='command')
config.bind('<Ctrl-d>', 'rl-delete-char', mode='command')
config.bind('<Ctrl-a>', 'rl-beginning-of-line', mode='command')
config.bind('<Ctrl-b>', 'rl-backward-char', mode='command')
config.bind('<Ctrl-e>', 'rl-end-of-line', mode='command')
config.bind('<Ctrl-f>', 'rl-forward-char', mode='command')
config.bind('<Ctrl-h>', 'rl-backward-delete-char', mode='command')
config.bind('<Ctrl-k>', 'rl-kill-line', mode='command')

# prompt mode
config.bind('<Ctrl-p>',       'prompt-item-focus prev', mode='prompt')
config.bind('<Up>',           'prompt-item-focus prev', mode='prompt')
config.bind('<Ctrl-n>',       'prompt-item-focus next', mode='prompt')
config.bind('<Down>',         'prompt-item-focus next', mode='prompt')
config.bind('<Ctrl-g>',       'leave-mode',             mode='prompt')
config.bind('<Escape>',       'leave-mode',             mode='prompt')
config.bind('<Ctrl-m>',       'prompt-accept',          mode='prompt')
config.bind('<Return>',       'prompt-accept',          mode='prompt')
config.bind('<Ctrl-Shift-i>', 'prompt-item-focus prev', mode='prompt')
config.bind('<Shift-Tab>',    'prompt-item-focus prev', mode='prompt')
config.bind('<Ctrl-i>',       'prompt-item-focus next', mode='prompt')
config.bind('<Tab>',          'prompt-item-focus next', mode='prompt')
config.bind('y',              'prompt-accept yes',      mode='yesno')
config.bind('n',              'prompt-accept no',       mode='yesno')
# I still have problems with prompt. The confirm is a trap I can't
# escape. Setting javascript.modal_dialog to True sort of solves that
# by having an extra window with clickable buttons. Not ideal, but it
# works until I found a better solution.
# https://www.w3schools.com/js/js_popup.asp                     # fine
# https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert   # fine
# https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm # temporary solution
# https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt  # fine
c.content.javascript.modal_dialog = True

# hinting
config.bind('o', 'hint')
config.bind('O', 'hint --rapid links tab-bg')
# config.bind('<Ctrl-B>', 'hint all tab-bg', mode='hint')
# config.bind('<Ctrl-F>', 'hint links', mode='hint')
config.bind('<Escape>', 'leave-mode', mode='hint')
config.bind('<Ctrl-g>', 'leave-mode', mode='hint')
config.bind('<Return>', 'follow-hint', mode='hint')
config.bind('<Ctrl-m>', 'follow-hint', mode='hint')

# mpv
config.bind('vv', 'spawn mpv --fs {url}')
config.bind('vo', 'hint --add-history links spawn mpv --fs {hint-url}')

c.completion.height = '30%'

# Empty whitelist
c.content.host_blocking.whitelist = []

# Start site
c.url.default_page = 'https://duckduckgo.com'
c.url.start_pages = 'https://duckduckgo.com'

# Search engines
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}',
                       'rr': 'https://reddit.com/r/{}',
                       'yy': 'https://www.youtube.com/results?search_query={}',
                       "osm": "https://www.openstreetmap.org/search?query={}",
                       'aw': 'https://wiki.archlinux.org/?search={}',
                       'w': 'https://en.wikipedia.org/?search={}',
}

# Code hints
c.hints.selectors["code"] = [
    # Selects all code tags whose direct parent is not a pre tag
    ":not(pre) > code",
    "pre"
]

config.bind('yc', 'hint code userscript code-select.py')

# Org Capture
config.bind('cl', "open javascript:location.href='org-protocol://store-link?url='+ encodeURIComponent(location.href);")
config.bind('cn', "open javascript:location.href='org-protocol://capture?template=n'")
config.bind('cb', "open javascript:location.href='org-protocol://capture-html?template=p&url=' + encodeURIComponent(location.href) + '&title=' + encodeURIComponent(document.title || '[untitled page]') + '&body=' + encodeURIComponent(function () {var html = ''; if (typeof document.getSelection != 'undefined') {var sel = document.getSelection(); if (sel.rangeCount) {var container = document.createElement('div'); for (var i = 0, len = sel.rangeCount; i < len; ++i) {container.appendChild(sel.getRangeAt(i).cloneContents());} html = container.innerHTML;}} else if (typeof document.selection != 'undefined') {if (document.selection.type == 'Text') {html = document.selection.createRange().htmlText;}} var relToAbs = function (href) {var a = document.createElement('a'); a.href = href; var abs = a.protocol + '//' + a.host + a.pathname + a.search + a.hash; a.remove(); return abs;}; var elementTypes = [['a', 'href'], ['img', 'src']]; var div = document.createElement('div'); div.innerHTML = html; elementTypes.map(function(elementType) {var elements = div.getElementsByTagName(elementType[0]); for (var i = 0; i < elements.length; i++) {elements[i].setAttribute(elementType[1], relToAbs(elements[i].getAttribute(elementType[1])));}}); return div.innerHTML;}());")
config.bind('cp', "spawn emacsclient org-protocol://capture?template=q&title={title}")

# Pass
config.bind('<z><l>', 'spawn --userscript qute-pass')
config.bind('<z><u><l>', 'spawn --userscript qute-pass --username-only')
config.bind('<z><p><l>', 'spawn --userscript qute-pass --password-only')
config.bind('<z><o><l>', 'spawn --userscript qute-pass --otp-only')
config.bind('<Alt+Shift+P>', 'spawn passmenu')

# Other settings
c.auto_save.session = True
c.content.autoplay = False
c.content.pdfjs = True
c.scrolling.smooth = True
c.tabs.background = True
c.completion.use_best_match = True # fuzzy matching
c.tabs.new_position.unrelated = "next"

c.content.geolocation = 'ask'
c.content.headers.do_not_track = True

c.fonts.monospace = '"Hack", "xos4 Terminus", Terminus, Monospace, "DejaVu Sans Mono", Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'
c.qt.highdpi = True

c.downloads.remove_finished = 1000
c.tabs.mousewheel_switching = False
