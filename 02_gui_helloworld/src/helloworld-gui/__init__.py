import PySimpleGUI as sg


def just_return_true():
    """Used for unit test ilustration."""
    return True


def open_main_window():
    """Construct and show the window."""
    main_window = sg.Window(
        title="This is the GUI",
        layout=[[
            sg.Text('Hello World!')
        ]],
        margins=(200, 50)
    )
    main_window.read()
