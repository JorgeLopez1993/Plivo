from plivo import plivoxml
get_digits=plivoxml.ResponseElement()
get_digits.add(
plivoxml.GetDigitsElement(action='ttps://ugyn9ecx0a.execute-api.eu-west-1.amazonaws.com/prod/plivonumber5', method='POST').add(
plivoxml.SpeakElement('Pulse 5 para aceptar el mensaje y 9 para repetirlo')))
print(get_digits.to_string())
