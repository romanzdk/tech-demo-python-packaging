import PySimpleGUI as sg


def open_main_window():
    """Construct and show the window."""
    main_window = sg.Window(
        title=_('This is the GUI'),
        layout=[[
            sg.Text(_('Hello World!'))
        ]],
        margins=(200, 50)
    )
    main_window.read()
