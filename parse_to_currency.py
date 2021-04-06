def format_to_currency(hex_value: str = '20A6', number: float = 0) -> str:
    int_representation_of_hex = ""
    if hex_value is not None and isinstance(hex_value, str):
        try:
            int_representation_of_hex = int(hex_value, 16)
        except ValueError as _:
            return "invalid function argument passed, can't convert hex value to integer"
        return f"{chr(int_representation_of_hex)}{number:,.2f}"
    return f"{int_representation_of_hex}{str(number)}"
