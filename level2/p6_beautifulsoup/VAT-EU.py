from bs4 import BeautifulSoup
import requests
import mechanize

def verify_vat_EU(vateu:str):
    responseDictionary = {}
    countryCode = vateu[:2]
    pureNumber = vateu[2:]

    # initialize mechanize browser and form
    br = mechanize.Browser()
    br.open('https://ec.europa.eu/taxation_customs/vies/vatRequest.html')
    response = br.response()
    br.select_form('vowRequestForm')

    # setup post form
    br.form['memberStateCode'] = [countryCode]
    br.form['number'] = pureNumber

    # submit post form, and close connection
    br.submit()
    soup = BeautifulSoup(br.response().read(), 'html.parser')
    br.close()

    # response table
    g = soup.find(id="vatResponseFormTable")
    #print(g)

    # console response -- not important
    responseType = str(g.b)
    if responseType.__contains__('Yes'):
        responseType = responseType[28:-11]
    else:
        responseType = responseType[30:-111]
    print(responseType)

    # setup response -- main refactoring of code
    if responseType.__contains__('Yes'):
        labele = g.find_all("td")
        member_state = str(labele[2])[23:-5]
        member_state_value = str(labele[3])[4:-5]
        vat_number = str(labele[5])[23:-5]
        vat_number_value = str(labele[6])[4:-5]
        data_request = str(labele[7])[23:-5]
        data_request_value = str(labele[8])[4:-5]
        vat_name = str(labele[9])[23:-5]
        vat_name_value = str(labele[10])[4:-6]
        adress = str(labele[11])[23:-5]
        adress_line_two = 'Adress Line Two'
        adress_value_one = str(labele[12])[4:-28]
        adress_value_two = str(labele[12])[26:-6]
        responseDictionary[member_state] = member_state_value
        responseDictionary[vat_number] = vat_number_value
        responseDictionary[data_request] = data_request_value
        responseDictionary[vat_name] = vat_name_value
        responseDictionary[adress] = adress_value_one
        responseDictionary[adress_line_two] = adress_value_two
        return responseDictionary
    else:
        return {"request":"not_valid"}

#[*, AT, BE, BG, CY, CZ, DE, DK, EE, EL, ES, FI, FR, GB, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK]
# OBSLUGIWANE KRAJE DO POCZĄTKU NUMERU

print(verify_vat_EU('ATU63422709'))
print(verify_vat_EU('PLU654645'))

"""
Treść Forma:
Trzeba wybrać selecta:
<SelectControl(memberStateCode=[*, AT, BE, BG, CY, CZ, DE, DK, EE, EL, ES, FI, FR, GB, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK])>
  <TextControl(<None>=--) (disabled)>
  <TextControl(number=)>
  <TextControl(traderName=)>
  <SelectControl(traderCompanyType=[])>
  <TextControl(traderStreet=)>
  <TextControl(traderPostalCode=)>
  <TextControl(traderCity=)>
  <SelectControl(requesterMemberStateCode=[*, AT, BE, BG, CY, CZ, DE, DK, EE, EL, ES, EU, FI, FR, GB, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK])>
  <TextControl(<None>=) (disabled)>
  <TextControl(requesterNumber=)>
  <HiddenControl(action=check) (readonly)>
  <SubmitControl(check=Verify) (readonly)>>

"""