import nicegui


def sumar():
    try:
        n1 = float(numero1.value)
        n2 = float(numero2.value)
        total = n1 + n2
        resultado.text = f'Resultado: {total:g}'
    except (TypeError, ValueError):
        resultado.text = 'Ingresa números válidos'


def limpiar():
    numero1.value = ''
    numero2.value = ''
    resultado.text = 'Resultado: 0'


with nicegui.ui.column().classes(
    'w-full h-screen items-center justify-center'
):
    with nicegui.ui.card().style(
        'width:400px; background-color:purple;'
    ).classes('items-center'):

        nicegui.ui.label(
            'Calculadora de Suma'
        ).style(
            'color:white; font-size:24px; font-weight:bold'
        )

        numero1 = nicegui.ui.input('Número 1').props(
            'dark outlined'
        ).style('width:300px')

        numero2 = nicegui.ui.input('Número 2').props(
            'dark outlined'
        ).style('width:300px')

        with nicegui.ui.row():
            nicegui.ui.button('Sumar', on_click=sumar).props('color=green')
            nicegui.ui.button('Limpiar', on_click=limpiar).props('color=red')

        resultado = nicegui.ui.label('Resultado: 0').style(
            'color:white; font-size:20px'
        )

nicegui.ui.run()