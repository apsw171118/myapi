from flask import Flask, jsonify, request, send_from_directory, url_for
import requests, os


app = Flask(__name__)

apikeylist = [
    "8yCEm6ekTJZ0rx4DfXNphuEB0arT5okuGMqFuW4wqIjbaqewkYcqsjK2MfKct3xJHdEhA80DSLv5VtxP8RTZMRthEWpFO9gtzlVYVJnbbsNyajB0Hqg0rKKviZgC2hu8"
]


@app.route("/")
def hello():
    return jsonify(
        {
            "message": "this is a private api. please email me@msft.joshuang.site for access"
        }
    )


@app.route("/api/v1/health")
def health_check():
    return jsonify({"status": "healthy"})


@app.route("/currency/convert")
def currencynameconvert():
    text = request.args.get("text", None)
    apikey = request.args.get("apikey", None)
    if not apikey:
        return jsonify({"error": "apikey is required"})
    if not apikey in apikeylist:
        return jsonify({"error": "invalid apikey"})
    if not text:
        return jsonify({"error": "text is required"})

    currency_codes = {
        "Australian Dollar (AUD)": "AUD",
        "Bulgarian Lev (BGN)": "BGN",
        "Brazilian Real (BRL)": "BRL",
        "Canadian Dollar (CAD)": "CAD",
        "Swiss Franc (CHF)": "CHF",
        "Chinese Yuan (CNY)": "CNY",
        "Czech Koruna (CZK)": "CZK",
        "Danish Krone (DKK)": "DKK",
        "Euro (EUR)": "EUR",
        "Great British Pound (GBP)": "GBP",
        "Hong Kong Dollar (HKD)": "HKD",
        "Hungarian Forint (HUF)": "HUF",
        "Indonesian Rupiah (IDR)": "IDR",
        "Israeli New Shekel (ILS)": "ILS",
        "Indian Rupee (INR)": "INR",
        "Icelandic Krona (ISK)": "ISK",
        "Japanese Yen (JPY)": "JPY",
        "South Korean Won (KRW)": "KRW",
        "Mexican Peso (MXN)": "MXN",
        "Malaysian Ringgit (MYR)": "MYR",
        "Norwegian Krone (NOK)": "NOK",
        "New Zealand Dollar (NZD)": "NZD",
        "Philippine Peso (PHP)": "PHP",
        "Polish Zloty (PLN)": "PLN",
        "Romanian Leu (RON)": "RON",
        "Swedish Krona (SEK)": "SEK",
        "Singapore Dollar (SGD)": "SGD",
        "Thai Baht (THB)": "THB",
        "Turkish Lira (TRY)": "TRY",
        "United States Dollar (USD)": "USD",
        "South African Rand (ZAR)": "ZAR",
    }

    currency_code = currency_codes.get(text)

    if currency_code:
        return jsonify({"currency": text, "code": currency_code})
    else:
        return jsonify({"error": f"Currency code for '{text}' not found"}), 404


@app.route("/currency")
def currency():
    fromc = request.args.get("fromc", "GBP")
    toc = request.args.get("toc", "USD")
    options = request.args.get("extra", None)
    apikey = request.args.get("apikey", None)
    if not apikey:
        return jsonify({"error": "apikey is required"})
    if not apikey in apikeylist:
        return
    response = requests.get(f"https://api.vatcomply.com/rates?base={fromc}")
    data = response.json()
    if options:
        return jsonify(data)
    if toc in data["rates"]:
        rate = data["rates"][toc]
        return jsonify({"from": fromc, "to": toc, "rate": rate})
    else:
        return jsonify({"error": f"Exchange rate for {toc} not found"}), 404


@app.route("/currency/methods")
def currencyroutes():
    return jsonify(
        {
            "AUD": "Australian Dollar",
            "BGN": "Bulgarian Lev",
            "BRL": "Brazilian Real",
            "CAD": "Canadian Dollar",
            "CHF": "Swiss Franc",
            "CNY": "Chinese Yuan",
            "CZK": "Czech Koruna",
            "DKK": "Danish Krone",
            "EUR": "Euro",
            "GBP": "Great British Pound",
            "HKD": "Hong Kong Dollar",
            "HUF": "Hungarian Forint",
            "IDR": "Indonesian Rupiah",
            "ILS": "Israeli New Shekel",
            "INR": "Indian Rupee",
            "ISK": "Icelandic Krona",
            "JPY": "Japanese Yen",
            "KRW": "South Korean Won",
            "MXN": "Mexican Peso",
            "MYR": "Malaysian Ringgit",
            "NOK": "Norwegian Krone",
            "NZD": "New Zealand Dollar",
            "PHP": "Philippine Peso",
            "PLN": "Polish Zloty",
            "RON": "Romanian Leu",
            "SEK": "Swedish Krona",
            "SGD": "Singapore Dollar",
            "THB": "Thai Baht",
            "TRY": "Turkish Lira",
            "USD": "United States Dollar",
            "ZAR": "South African Rand",
        }
    )


@app.route("/flag")
def serve_asset():
    flag = request.args.get("flag", None)
    apikey = request.args.get("apikey", None)
    if not apikey:
        return jsonify({"error": "apikey is required"})
    if not apikey in apikeylist:
        return
    if not flag:
        return jsonify({"error": "flag is required"})
    return send_from_directory(os.path.join("../assets"), f"{flag}.png")


@app.route("/convertcountryname")
def convert_country_name():
    name = request.args.get("name", None)
    apikey = request.args.get("apikey", None)
    if not apikey:
        return jsonify({"error": "apikey is required"})
    if not apikey in apikeylist:
        return jsonify({"error": "invalid apikey"})
    if not name:
        return jsonify({"error": "name is required"})

    countryname = {
        "Andorra": "ad",
        "United Arab Emirates": "ae",
        "Afghanistan": "af",
        "Antigua and Barbuda": "ag",
        "Anguilla": "ai",
        "Albania": "al",
        "Armenia": "am",
        "Angola": "ao",
        "Antarctica": "aq",
        "Argentina": "ar",
        "American Samoa": "as",
        "Austria": "at",
        "Australia": "au",
        "Aruba": "aw",
        "Åland Islands": "ax",
        "Azerbaijan": "az",
        "Bosnia and Herzegovina": "ba",
        "Barbados": "bb",
        "Bangladesh": "bd",
        "Belgium": "be",
        "Burkina Faso": "bf",
        "Bulgaria": "bg",
        "Bahrain": "bh",
        "Burundi": "bi",
        "Benin": "bj",
        "Saint Barthélemy": "bl",
        "Bermuda": "bm",
        "Brunei": "bn",
        "Bolivia": "bo",
        "Bonaire, Sint Eustatius and Saba": "bq",
        "Brazil": "br",
        "Bahamas": "bs",
        "Bhutan": "bt",
        "Bouvet Island": "bv",
        "Botswana": "bw",
        "Belarus": "by",
        "Belize": "bz",
        "Canada": "ca",
        "Cocos (Keeling) Islands": "cc",
        "Congo, Democratic Republic of the": "cd",
        "Central African Republic": "cf",
        "Congo, Republic of the": "cg",
        "Switzerland": "ch",
        "Ivory Coast": "ci",
        "Cook Islands": "ck",
        "Chile": "cl",
        "Cameroon": "cm",
        "China": "cn",
        "Colombia": "co",
        "Costa Rica": "cr",
        "Cuba": "cu",
        "Cape Verde": "cv",
        "Curaçao": "cw",
        "Christmas Island": "cx",
        "Cyprus": "cy",
        "Czech Republic": "cz",
        "Germany": "de",
        "Djibouti": "dj",
        "Denmark": "dk",
        "Dominica": "dm",
        "Dominican Republic": "do",
        "Algeria": "dz",
        "Ecuador": "ec",
        "Estonia": "ee",
        "Egypt": "eg",
        "Western Sahara": "eh",
        "Eritrea": "er",
        "Spain": "es",
        "Ethiopia": "et",
        "Finland": "fi",
        "Fiji": "fj",
        "Falkland Islands": "fk",
        "Federated States of Micronesia": "fm",
        "Faroe Islands": "fo",
        "France": "fr",
        "Gabon": "ga",
        "England": "gb-eng",
        "Northern Ireland": "gb-nir",
        "Scotland": "gb-sct",
        "Wales": "gb-wls",
        "United Kingdom": "gb",
        "Grenada": "gd",
        "Georgia": "ge",
        "French Guiana": "gf",
        "Guernsey": "gg",
        "Ghana": "gh",
        "Gibraltar": "gi",
        "Greenland": "gl",
        "Gambia": "gm",
        "Guinea": "gn",
        "Guadeloupe": "gp",
        "Equatorial Guinea": "gq",
        "Greece": "gr",
        "South Georgia and the South Sandwich Islands": "gs",
        "Guatemala": "gt",
        "Guam": "gu",
        "Guinea-Bissau": "gw",
        "Guyana": "gy",
        "Hong Kong": "hk",
        "Heard Island and McDonald Islands": "hm",
        "Honduras": "hn",
        "Croatia": "hr",
        "Haiti": "ht",
        "Hungary": "hu",
        "Indonesia": "id",
        "Ireland": "ie",
        "Israel": "il",
        "Isle of Man": "im",
        "India": "in",
        "British Indian Ocean Territory": "io",
        "Iraq": "iq",
        "Iran": "ir",
        "Iceland": "is",
        "Italy": "it",
        "Jersey": "je",
        "Jamaica": "jm",
        "Jordan": "jo",
        "Japan": "jp",
        "Kenya": "ke",
        "Kyrgyzstan": "kg",
        "Cambodia": "kh",
        "Kiribati": "ki",
        "Comoros": "km",
        "Saint Kitts and Nevis": "kn",
        "North Korea": "kp",
        "South Korea": "kr",
        "Kuwait": "kw",
        "Cayman Islands": "ky",
        "Kazakhstan": "kz",
        "Laos": "la",
        "Lebanon": "lb",
        "Saint Lucia": "lc",
        "Liechtenstein": "li",
        "Sri Lanka": "lk",
        "Liberia": "lr",
        "Lesotho": "ls",
        "Lithuania": "lt",
        "Luxembourg": "lu",
        "Latvia": "lv",
        "Libya": "ly",
        "Morocco": "ma",
        "Monaco": "mc",
        "Moldova": "md",
        "Montenegro": "me",
        "Saint Martin": "mf",
        "Madagascar": "mg",
        "Marshall Islands": "mh",
        "North Macedonia": "mk",
        "Mali": "ml",
        "Myanmar": "mm",
        "Mongolia": "mn",
        "Macao": "mo",
        "Northern Mariana Islands": "mp",
        "Martinique": "mq",
        "Mauritania": "mr",
        "Montserrat": "ms",
        "Malta": "mt",
        "Mauritius": "mu",
        "Maldives": "mv",
        "Malawi": "mw",
        "Mexico": "mx",
        "Malaysia": "my",
        "Mozambique": "mz",
        "Namibia": "na",
        "New Caledonia": "nc",
        "Niger": "ne",
        "Norfolk Island": "nf",
        "Nigeria": "ng",
        "Nicaragua": "ni",
        "Netherlands": "nl",
        "Norway": "no",
        "Nepal": "np",
        "Nauru": "nr",
        "Niue": "nu",
        "New Zealand": "nz",
        "Oman": "om",
        "Panama": "pa",
        "Peru": "pe",
        "French Polynesia": "pf",
        "Papua New Guinea": "pg",
        "Philippines": "ph",
        "Pakistan": "pk",
        "Poland": "pl",
        "Saint Pierre and Miquelon": "pm",
        "Pitcairn Islands": "pn",
        "Puerto Rico": "pr",
        "Palestine": "ps",
        "Portugal": "pt",
        "Palau": "pw",
        "Paraguay": "py",
        "Qatar": "qa",
        "Réunion": "re",
        "Romania": "ro",
        "Serbia": "rs",
        "Russia": "ru",
        "Rwanda": "rw",
        "Saudi Arabia": "sa",
        "Solomon Islands": "sb",
        "Seychelles": "sc",
        "Sudan": "sd",
        "Sweden": "se",
        "Singapore": "sg",
        "Saint Helena": "sh",
        "Slovenia": "si",
        "Svalbard and Jan Mayen": "sj",
        "Slovakia": "sk",
        "Sierra Leone": "sl",
        "San Marino": "sm",
        "Senegal": "sn",
        "Somalia": "so",
        "Suriname": "sr",
        "South Sudan": "ss",
        "São Tomé and Príncipe": "st",
        "El Salvador": "sv",
        "Sint Maarten": "sx",
        "Syria": "sy",
        "Eswatini": "sz",
        "Turks and Caicos Islands": "tc",
        "Chad": "td",
        "French Southern Territories": "tf",
        "Togo": "tg",
        "Thailand": "th",
        "Tajikistan": "tj",
        "Tokelau": "tk",
        "Timor-Leste": "tl",
        "Turkmenistan": "tm",
        "Tunisia": "tn",
        "Tonga": "to",
        "Turkey": "tr",
        "Trinidad and Tobago": "tt",
        "Tuvalu": "tv",
        "Tanzania": "tz",
        "Ukraine": "ua",
        "Uganda": "ug",
        "United States Minor Outlying Islands": "um",
        "United States": "us",
        "Uruguay": "uy",
        "Uzbekistan": "uz",
        "Vatican City": "va",
        "Saint Vincent and the Grenadines": "vc",
        "Venezuela": "ve",
        "British Virgin Islands": "vg",
        "United States Virgin Islands": "vi",
        "Vietnam": "vn",
        "Vanuatu": "vu",
        "Wallis and Futuna": "wf",
        "Samoa": "ws",
        "Kosovo": "xk",
        "Yemen": "ye",
        "Mayotte": "yt",
        "South Africa": "za",
        "Zambia": "zm",
        "Zimbabwe": "zw",
    }

    code = countryname.get(name)
    if code:
        return jsonify({"country": name, "code": code})
    else:
        return jsonify({"error": f"Country code for '{name}' not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
