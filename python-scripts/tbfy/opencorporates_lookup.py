# -*- coding: utf-8 -*-

# ***************************************************************************************************
# Data ingestion script for the TBFY Knowledge Graph (https://theybuyforyou.eu/tbfy-knowledge-graph/)
# 
# This file contains a lookup/conversion table to be used for country names according 
# to https://en.wikipedia.org/wiki/ISO_3166-1
#
# Copyright: SINTEF 2017-2020
# Author   : Brian Elvesæter (brian.elvesater@sintef.no)
# License  : Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
# Project  : Developed as part of the TheyBuyForYou project (https://theybuyforyou.eu/)
# Funding  : TheyBuyForYou has received funding from the European Union's Horizon 2020
#            research and innovation programme under grant agreement No 780247
# ***************************************************************************************************

country_name_codes = {
    "afghanistan": "af",
    "af": "af",
    "åland islands": "ax",
    "albania": "al",
    "al": "al",
    "algeria": "dz",
    "dz": "dz",
    "american samoa": "as",
    "as": "as",
    "andorra": "ad",
    "ad": "ad",
    "angola": "ao",
    "ao": "ao",
    "anguilla": "ai",
    "ai": "ai",
    "antarctica": "aq",
    "aq": "aq",
    "antigua and barbuda": "ag",
    "ag": "ag",
    "argentina": "ar",
    "ar": "ar",
    "armenia": "am",
    "am": "am",
    "aruba": "aw",
    "aw": "aw",
    "australia": "au",
    "au": "au",
    "austria": "at",
    "at": "at",
    "azerbaijan": "az",
    "az": "az",
    "bahamas": "bs",
    "bs": "bs",
    "bahrain": "bh",
    "bh": "bh",
    "bangladesh": "bd",
    "bd": "bd",
    "barbados": "bb",
    "bb": "bb",
    "belarus": "by",
    "by": "by",
    "belgium": "be",
    "be": "be",
    "belize": "bz",
    "bz": "bz",
    "benin": "bj",
    "bj": "bj",
    "bermuda": "bm",
    "bm": "bm",
    "bhutan": "bt",
    "bt": "bt",
    "bolivia (plurinational state of)": "bo",
    "bolivia": "bo",
    "bo": "bo",
    "bonaire, sint eustatius and saba": "bq",
    "bq": "bq",
    "bosnia and herzegovina": "ba",
    "ba": "ba",
    "botswana": "bw",
    "bw": "bw",
    "bouvet island": "bv",
    "bv": "bv",
    "brazil": "br",
    "br": "br",
    "british indian ocean territory": "io",
    "io": "io",
    "brunei darussalam": "bn",
    "bn": "bn",
    "bulgaria": "bg",
    "bg": "bg",
    "burkina faso": "bf",
    "bf": "bf",
    "burundi": "bi",
    "bi": "bi",
    "cabo verde": "cv",
    "cv": "cv",
    "cambodia": "kh",
    "kh": "kh",
    "cameroon": "cm",
    "cm": "cm",
    "canada" : "ca",
    "ca": "ca",
    "cayman islands": "ky",
    "ky": "ky",
    "central african republic": "cf",
    "cf": "cf",
    "chad": "td",
    "td": "td",
    "chile": "cl",
    "cl": "cl",
    "china": "cn",
    "cn": "cn",
    "christmas island": "cx",
    "cx": "cx",
    "cocos (keeling) islands": "cc",
    "cocos keeling islands": "cc",
    "cocos islands": "cc",
    "cc": "cc",
    "colombia": "co",
    "co": "co",
    "comoros": "km",
    "km": "km",
    "congo": "cg",
    "cg": "cg",
    "congo, democratic republic of the": "cd",
    "democratic republic of the congo": "cd",
    "cd": "cd",
    "cook islands": "ck",
    "ck": "ck",
    "costa rica": "cr",
    "cr": "cr",
    "côte d'ivoire": "ci",
    "cote d'ivoire": "ci",
    "ci": "ci",
    "croatia": "hr",
    "hr": "hr",
    "cuba": "cu",
    "cu": "cu",
    "curaçao": "cw",
    "curacao": "cw",
    "cw": "cw",
    "cyprus": "cy",
    "cy": "cy",
    "czechia": "cz",
    "czech republic": "cz",
    "cz": "cz",
    "denmark": "dk",
    "dk": "dk",
    "djibouti": "dj",
    "dj": "dj",
    "dominica": "dm",
    "dm": "dm",
    "dominican republic": "do",
    "do": "do",
    "ecuador": "ec",
    "ec": "ec",
    "egypt": "eg",
    "eg": "eg",
    "el salvador": "sv",
    "sv": "sv",
    "equatorial guinea": "gq",
    "gq": "gq",
    "eritrea": "er",
    "er": "er",
    "estonia": "ee",
    "ee": "ee",
    "eswatini": "sz",
    "sz": "sz",
    "ethiopia": "et",
    "et": "et",
    "falkland islands (malvinas)": "fk",
    "falkland islands": "fk",
    "fk": "fk",
    "faroe islands": "fo",
    "fo": "fo",
    "fiji": "fj",
    "fj": "fj",
    "finland": "fi",
    "fi": "fi",
    "france": "fr",
    "fr": "fr",
    "french guiana": "gf",
    "gf": "gf",
    "french polynesia": "pf",
    "pf": "pf",
    "french southern territories": "tf",
    "tf": "tf",
    "gabon": "ga",
    "ga": "ga",
    "gambia": "gm",
    "gm": "gm",
    "georgia": "ge",
    "ge": "ge",
    "germany": "de",
    "de": "de",
    "ghana": "gh",
    "gh": "gh",
    "gibraltar": "gi",
    "gi": "gi",
    "greece": "gr",
    "gr": "gr",
    "greenland": "gl",
    "gl": "gl",
    "grenada": "gd",
    "gd": "gd",
    "guadeloupe": "gp",
    "gp": "gp",
    "guam": "gu",
    "gu": "gu",
    "guatemala": "gt",
    "gt": "gt",
    "guernsey": "gg",
    "gg": "gg",
    "guinea": "gn",
    "gn": "gn",
    "guinea-bissau": "gw",
    "gw": "gw",
    "guyana": "gy",
    "gy": "gy",
    "haiti": "ht",
    "ht": "ht",
    "heard island and mcdonald islands": "hm",
    "hm": "hm",
    "holy see": "va",
    "va": "va",
    "honduras": "hn",
    "hn": "hn",
    "hong kong": "hk",
    "hk": "hk",
    "hungary": "hu",
    "hu": "hu",
    "iceland": "is",
    "is": "is",
    "india": "in",
    "in": "in",
    "indonesia": "id",
    "id": "id",
    "iran (islamic republic of)": "ir",
    "islamic republic of iran": "ir",
    "iran": "ir",
    "ir": "ir",
    "iraq": "iq",
    "iq": "iq",
    "ireland": "ie",
    "ie": "ie",
    "isle of man": "im",
    "im": "im",
    "israel": "il",
    "il": "il",
    "italy": "it",
    "it": "it",
    "jamaica": "jm",
    "jm": "jm",
    "japan": "jp",
    "jp": "jp",
    "jersey": "je",
    "je": "je",
    "jordan": "jo",
    "jo": "jo",
    "kazakhstan": "kz",
    "kz": "kz",
    "kenya": "ke",
    "ke": "ke",
    "kiribati": "ki",
    "ki": "ki",
    "korea (democratic people's republic of)": "kp",
    "democratic people's republic of korea": "kp",
    "kp": "kp",
    "korea, republic of": "kr",
    "republic of korea": "kr",
    "korea": "kr",
    "kr": "kr",
    "kuwait": "kw",
    "kw": "kw",
    "kyrgyzstan": "kg",
    "kg": "kg",
    "lao people's democratic republic": "la",
    "la": "la",
    "latvia": "lv",
    "lv": "lv",
    "lebanon": "lb",
    "lb": "lb",
    "lesotho": "ls",
    "ls": "ls",
    "liberia": "lr",
    "lr": "lr",
    "libya": "ly",
    "ly": "ly",
    "liechtenstein": "li",
    "li": "li",
    "lithuania": "lt",
    "lt": "lt",
    "luxembourg": "lu",
    "lu": "lu",
    "macao": "mo",
    "mo": "mo",
    "madagascar": "mg",
    "mg": "mg",
    "malawi": "mw",
    "mw": "mw",
    "malaysia": "my",
    "my": "my",
    "maldives": "mv",
    "mv": "mv",
    "mali": "ml",
    "ml": "ml",
    "malta": "mt",
    "mt": "mt",
    "marshall islands": "mh",
    "mh": "mh",
    "martinique": "mq",
    "mq": "mq",
    "mauritania": "mr",
    "mr": "mr",
    "mauritius": "mu",
    "mu": "mu",
    "mayotte": "yt",
    "yt": "yt",
    "mexico": "mx",
    "mx": "mx",
    "micronesia (federated states of)": "fm",
    "federated states of micronesia": "fm",
    "micronesia": "fm",
    "fm": "fm",
    "moldova, republic of": "md",
    "republic of moldova": "md",
    "moldova": "md",
    "md": "md",
    "monaco": "mc",
    "mc": "mc",
    "mongolia": "mn",
    "mn": "mn",
    "montenegro": "me",
    "me": "me",
    "montserrat": "ms",
    "ms": "ms",
    "morocco": "ma",
    "ma": "ma",
    "mozambique": "mz",
    "mz": "mz",
    "myanmar": "mm",
    "mm": "mm",
    "namibia": "na",
    "na": "na",
    "nauru": "nr",
    "nr": "nr",
    "nepal": "np",
    "np": "np",
    "netherlands": "nl",
    "nl": "nl",
    "new caledonia": "nc",
    "nc": "nc",
    "new zealand": "nz",
    "nz": "nz",
    "nicaragua": "ni",
    "ni": "ni",
    "niger": "ne",
    "ne": "ne",
    "nigeria": "ng",
    "ng": "ng",
    "niue": "nu",
    "nu": "nu",
    "norfolk island": "nf",
    "nf": "nf",
    "macedonia": "mk",
    "north macedonia": "mk",
    "mk": "mk",
    "northern mariana islands": "mp",
    "mp": "mp",
    "norway": "no",
    "no": "no",
    "oman": "om",
    "om": "om",
    "pakistan": "pk",
    "pk": "pk",
    "palau": "pw",
    "pw": "pw",
    "palestine, state of": "ps",
    "state of palestine": "ps",
    "palestine": "ps",
    "ps": "ps",
    "panama": "pa",
    "pa": "pa",
    "papua new guinea": "pg",
    "pg": "pg",
    "paraguay": "py",
    "py": "py",
    "peru": "pe",
    "pe": "pe",
    "philippines": "ph",
    "ph": "ph",
    "pitcairn": "pn",
    "pn": "pn",
    "poland": "pl",
    "pl": "pl",
    "portugal": "pt",
    "pt": "pt",
    "puerto rico": "pr",
    "pr": "pr",
    "qatar": "qa",
    "qa": "qa",
    "réunion": "re",
    "reunion": "re",
    "re": "re",
    "romania": "ro",
    "ro": "ro",
    "russian federation": "ru",
    "russia": "ru",
    "ru": "ru",
    "rwanda": "rw",
    "rw": "rw",
    "saint barthélemy": "bl",
    "saint barthelemy": "bl",
    "bl": "bl",
    "saint helena, ascension and tristan da cunha": "sh",
    "saint helena": "sh",
    "sh": "sh",
    "saint kitts and nevis": "kn",
    "kn": "kn",
    "saint lucia": "lc",
    "lc": "lc",
    "saint martin (french part)": "mf",
    "saint martin": "mf",
    "mf": "mf",
    "saint pierre and miquelon": "pm",
    "pm": "pm",
    "saint vincent and the grenadines": "vc",
    "vc": "vc",
    "samoa": "ws",
    "ws": "ws",
    "san marino": "sm",
    "sm": "sm",
    "sao tome and principe": "st",
    "st": "st",
    "saudi arabia": "sa",
    "sa": "sa",
    "senegal": "sn",
    "sn": "sn",
    "serbia": "rs",
    "rs": "rs",
    "seychelles": "sc",
    "sc": "sc",
    "sierra leone": "sl",
    "sl": "sl",
    "singapore": "sg",
    "sg": "sg",
    "sint maarten (dutch part)": "sx",
    "sint maarten": "sx",
    "sx": "sx",
    "slovakia": "sk",
    "sk": "sk",
    "slovenia": "si",
    "si": "si",
    "solomon islands": "sb",
    "sb": "sb",
    "somalia": "so",
    "so": "so",
    "south africa": "za",
    "za": "za",
    "south georgia and the south sandwich islands": "gs",
    "gs": "gs",
    "south sudan": "ss",
    "ss": "ss",
    "spain": "es",
    "es": "es",
    "sri lanka": "lk",
    "lk": "lk",
    "sudan": "sd",
    "sd": "sd",
    "suriname": "sr",
    "sr": "sr",
    "svalbard and jan mayen": "sj",
    "sj": "sj",
    "sweden": "se",
    "se": "se",
    "switzerland": "ch",
    "ch": "ch",
    "syrian arab republic": "sy",
    "sy": "sy",
    "taiwan, province of china": "tw",
    "taiwan": "tw",
    "tw": "tw",
    "tajikistan": "tj",
    "tj": "tj",
    "tanzania, united republic of": "tz",
    "united republic of tanzania": "tz",
    "tanzania": "tz",
    "tz": "tz",
    "thailand": "th",
    "th": "th",
    "timor-leste": "tl",
    "tl": "tl",
    "togo": "tg",
    "tg": "tg",
    "tokelau": "tk",
    "tk": "tk",
    "tonga": "to",
    "to": "to",
    "trinidad and tobago": "tt",
    "tt": "tt",
    "tunisia": "tn",
    "tn": "tn",
    "turkey": "tr",
    "tr": "tr",
    "turkmenistan": "tm",
    "tm": "tm",
    "turks and caicos islands": "tc",
    "tc": "tc",
    "tuvalu": "tv",
    "tv": "tv",
    "uganda": "ug",
    "ug": "ug",
    "ukraine": "ua",
    "ua": "ua",
    "united arab emirates": "ae",
    "ae": "ae",
    "united kingdom of great britain and northern ireland": "gb",
    "united kingdom": "gb",
    "great britain": "gb",
    "uk": "gb",
    "gb": "gb",
    "united states of america": "us",
    "usa": "us",
    "us": "us",
    "united states minor outlying islands": "um",
    "um": "um",
    "uruguay": "uy",
    "uy": "uy",
    "uzbekistan": "uz",
    "uz": "uz",
    "vanuatu": "vu",
    "vu": "vu",
    "venezuela (bolivarian republic of)": "ve",
    "bolivarian republic of venezuela": "ve",
    "venezuela": "ve",
    "ve": "ve",
    "viet nam": "vn",
    "vn": "vn",
    "virgin islands (british)": "vg",
    "vg": "vg",
    "virgin islands (u.s.)": "vi",
    "vi": "vi",
    "wallis and futuna": "wf",
    "wf": "wf",
    "western sahara": "eh",
    "eh": "eh",
    "yemen": "ye",
    "ye": "ye",
    "zambia": "zm",
    "zm": "zm",
    "zimbabwe": "zw",
    "zw": "zw",
}
