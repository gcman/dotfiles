((nil . ((eval . (add-hook 'after-save-hook
                           (lambda nil
                             (when (string-match-p "^~/dotfiles" default-directory)
                               (shell-command "stow .")))
                           nil t)))))
