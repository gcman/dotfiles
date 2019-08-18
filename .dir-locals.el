((nil
  (eval add-hook 'after-save-hook
        (lambda nil
          (let
              ((default-directory "~/dotfiles"))
            (shell-command "stow .")))
        nil t)))
