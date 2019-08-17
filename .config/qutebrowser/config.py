# Unbind some standard qutebrowser bindings
c.bindings.default = {}
# If you don't want to unbind everything it might be necessary to
# unbind at least the conflicting keybindings like this:

def bind_chained(key, *commands):
    config.bind(key, ' ;; '.join(commands))

# Don't have to always press Shift    
config.bind(';', 'set-cmd-text :')
    
# Reload config
config.bind('<Ctrl-x><Ctrl-l>', 'config-source')

config. bind('<Alt-e>', 'open-editor', mode='insert')
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
config.bind('<Ctrl-y>', 'insert-text {clipboard}', mode='insert')
config.bind('<Ctrl-y>', 'set-cmd-text -a {clipboard}', mode='command')

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
config.bind('<Ctrl-e>', 'fake-key <End>', mode='insert')
config.bind('<Ctrl-n>', 'fake-key <Down>', mode='insert')
config.bind('<Ctrl-p>', 'fake-key <Up>', mode='insert')
config.bind('<Alt-v>', 'fake-key <PgUp>', mode='insert')
config.bind('<Ctrl-v>', 'fake-key <PgDown>', mode='insert')
config.bind('<Alt-f>', 'fake-key <Ctrl-Right>', mode='insert')
config.bind('<Alt-b>', 'fake-key <Ctrl-Left>', mode='insert')
config.bind('<Ctrl-d>', 'fake-key <Delete>', mode='insert')
config.bind('<Alt-d>', 'fake-key <Ctrl-Delete>', mode='insert')
config.bind('<Ctrl-w>', 'fake-key <Ctrl-Backspace>', mode='insert')
config.bind('<Ctrl-y>', 'insert-text {primary}', mode='insert')

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
config.bind('bo', 'hint links tab-bg')
config.bind('O', 'hint --rapid links tab-bg')

config.bind('<Escape>', 'leave-mode', mode='hint')
config.bind('<Ctrl-g>', 'leave-mode', mode='hint')
config.bind('<Return>', 'follow-hint', mode='hint')
config.bind('<Ctrl-m>', 'follow-hint', mode='hint')

# mpv
config.bind('V', "spawn --userscript mpv-play.py")
config.bind('v', 'hint --add-history links userscript mpv-play.py')
config.bind('hv', 'hint --add-history --rapid links userscript mpv-play.py')
config.bind('<Ctrl-u>v', 'spawn --userscript ytdl.py')

# Code hints
c.hints.selectors["code"] = [
    # Selects all code tags whose direct parent is not a pre tag
    ":not(pre) > code",
    "pre"
]

config.bind('yc', 'hint code userscript code-select.py')
config.bind('yg', 'spawn --userscript github-copy.py')

# Org Capture
config.bind('cl', "spawn emacsclient org-protocol://store-link?url={url} ;; yank inline {url}")
config.bind('cn', "spawn emacsclient org-protocol://capture?template=n")
config.bind('cp', "spawn emacsclient org-protocol://capture?template=q&title={title}")
config.bind('cb', "spawn --userscript org-capture-bookmark.py")
config.bind('cc', "hint code userscript org-capture-code.py")

# Pass
config.bind('zl', 'spawn --userscript qute-pass')
config.bind('zul', 'spawn --userscript qute-pass --username-only')
config.bind('zpl', 'spawn --userscript qute-pass --password-only')
config.bind('zol', 'spawn --userscript qute-pass --otp-only')
config.bind('<Alt+Shift+P>', 'spawn passmenu')

# Torrent
config.bind('to', "hint links spawn emacsclient -e '(gm/transmission-add \"{hint-url}\")'")
config.bind('tO', "hint --rapid links spawn emacsclient -e '(gm/transmission-add \"{hint-url}\")'")

# Other settings
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
                       'car': 'https://carta.stanford.edu/course/{}'
}

c.content.host_blocking.whitelist = ['thepiratebay.org','adf.ly']
c.auto_save.session = True
c.content.autoplay = False
c.content.pdfjs = True
c.scrolling.smooth = True
c.tabs.background = True
c.completion.use_best_match = True # fuzzy matching
c.tabs.new_position.unrelated = "next"
c.new_instance_open_target = "tab-bg-silent"

c.content.geolocation = 'ask'
c.content.headers.do_not_track = True

c.fonts.monospace = '"Hack", "xos4 Terminus", Terminus, Monospace, "DejaVu Sans Mono", Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'
c.qt.highdpi = True

c.downloads.remove_finished = 1000
c.tabs.mousewheel_switching = False

c.content.headers.accept_language =  "en-US,en;q=0.5"
c.content.headers.custom = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}

c.aliases = {**c.aliases,
             "msg":"messages -t",
             "messages":"messages -t",
             "help":"help -t"}

