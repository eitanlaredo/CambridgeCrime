
# Define categories and their corresponding crime types


# Define categories and their corresponding crime types
larceny_crimes = [
        'Larceny (Misc)', 'Larceny from Building', 'Larceny from MV',
        'Larceny from Person', 'Larceny from Residence', 'Larceny of Bicycle',
        'Larceny of Plate', 'Larceny of Services'
    ],
fraud_financial_crimes = [
        'Forgery', 'Counterfeiting', 'Embezzlement', 'Flim Flam', 
        'Larceny of Services', 'Gambling'
    ],
violent_crimes = [
        'Aggravated Assault', 'Simple Assault', 'Homicide', 'Kidnapping', 
        'Street Robbery', 'Commercial Robbery', 'Domestic Dispute', 'Weapon Violations'
    ],
property_crimes = [
        'Commercial Break', 'Housebreak', 'Mal. Dest. Property', 'Arson', 
        'Rec. Stol. Property', 'Extortion/Blackmail', 'Burglary'
    ],
traffic_crimes =  [
        'Auto Theft', 'Hit and Run', 'OUI', 'Larceny of Bicycle', 'Larceny of Plate', 
        'Accident', 'Taxi Violation'
    ],
harassment_crimes =  [
        'Harassment', 'Indecent Exposure', 'Violation of R.O.', 
        'Violation of H.O.', 'Threats', 'Peeping & Spying', 
        'Sex Offender Violation', 'Stalking', 'Annoying & Accosting'
    ],
public_disorder_crimes =  [
        'Disorderly', 'Drinking in Public', 'Noise Complaint', 'Annoying & Accosting'
    ],
drug_crimes = [
        'Drugs', 'Liquor Possession/Sale', 'Drinking in Public', 'OUI'
    ],
prostitution_crimes =  [
        'Prostitution', 'Sex Offender Violation', 'Indecent Exposure'
    ],
warrant_crimes = [
        'Warrant Arrest', 'Disorderly', 'Violation of R.O.', 
        'Violation of H.O.', 'Stalking', 'Domestic Dispute'
    ],
misc_crimes =  [
        'Phone Calls', 'Missing Person', 'Suspicious Package'
    ]


CATEGORIES = {
    'Violent Crimes': [
        'Aggravated Assault', 'Simple Assault', 'Homicide', 'Kidnapping', 
        'Street Robbery', 'Commercial Robbery', 'Domestic Dispute', 'Weapon Violations'
    ],
    'Fraud And Financial Crimes': [
        'Forgery', 'Counterfeiting', 'Embezzlement', 'Flim Flam', 
        'Larceny of Services', 'Gambling'
    ],
    'Property Crimes': [
        'Commercial Break', 'Housebreak', 'Mal. Dest. Property', 'Arson', 
        'Rec. Stol. Property', 'Extortion/Blackmail', 'Burglary'
    ],
    'Traffic Related Crimes': [
        'Auto Theft', 'Hit and Run', 'OUI', 'Larceny of Bicycle', 'Larceny of Plate', 
        'Accident', 'Taxi Violation'
    ],
    'Larceny Crimes': [
        'Larceny (Misc)', 'Larceny from Building', 'Larceny from MV',
        'Larceny from Person', 'Larceny from Residence', 'Larceny of Bicycle',
        'Larceny of Plate', 'Larceny of Services'
    ],
    'Harassment Crimes': [
        'Harassment', 'Indecent Exposure', 'Violation of R.O.', 
        'Violation of H.O.', 'Threats', 'Peeping & Spying', 
        'Sex Offender Violation', 'Stalking', 'Annoying & Accosting'
    ],
    'Public Disorder': [
        'Disorderly', 'Drinking in Public', 'Noise Complaint', 'Annoying & Accosting'
    ],
    'Drugs and Related Crimes': [
        'Drugs', 'Liquor Possession/Sale', 'Drinking in Public', 'OUI'
    ],
    'Prostitution Related Crimes': [
        'Prostitution', 'Sex Offender Violation', 'Indecent Exposure'
    ],
    'Warrant Related Crimes': [
        'Warrant Arrest', 'Disorderly', 'Violation of R.O.', 
        'Violation of H.O.', 'Stalking', 'Domestic Dispute'
    ],
    'Misc. Crimes': [
        'Phone Calls', 'Missing Person', 'Suspicious Package'
    ]
}

APP_CATEGORIES = {
    'All Crimes': [
        'Larceny (Misc)', 'Larceny from Building', 'Larceny from MV',
        'Larceny from Person', 'Larceny from Residence', 'Larceny of Bicycle',
        'Larceny of Plate', 'Larceny of Services', 'Forgery', 'Counterfeiting',
        'Embezzlement', 'Flim Flam', 'Gambling', 'Aggravated Assault',
        'Simple Assault', 'Homicide', 'Kidnapping', 'Street Robbery',
        'Commercial Robbery', 'Domestic Dispute', 'Weapon Violations',
        'Commercial Break', 'Housebreak', 'Mal. Dest. Property', 'Arson',
        'Rec. Stol. Property', 'Extortion/Blackmail', 'Burglary', 'Auto Theft',
        'Hit and Run', 'OUI', 'Accident', 'Taxi Violation', 'Harassment',
        'Indecent Exposure', 'Violation of R.O.', 'Violation of H.O.',
        'Threats', 'Peeping & Spying', 'Sex Offender Violation', 'Stalking',
        'Annoying & Accosting', 'Disorderly', 'Drinking in Public',
        'Noise Complaint', 'Drugs', 'Liquor Possession/Sale', 'Prostitution',
        'Phone Calls', 'Missing Person', 'Suspicious Package'
    ],
    'Larceny Crimes': [
        'Larceny (Misc)', 'Larceny from Building', 'Larceny from MV',
        'Larceny from Person', 'Larceny from Residence', 'Larceny of Bicycle',
        'Larceny of Plate', 'Larceny of Services'
    ],
    'Fraud And Financial Crimes': [
        'Forgery', 'Counterfeiting', 'Embezzlement', 'Flim Flam', 
        'Larceny of Services', 'Gambling'
    ],
    'Violent Crimes': [
        'Aggravated Assault', 'Simple Assault', 'Homicide', 'Kidnapping', 
        'Street Robbery', 'Commercial Robbery', 'Domestic Dispute', 'Weapon Violations'
    ],
    'Property Crimes': [
        'Commercial Break', 'Housebreak', 'Mal. Dest. Property', 'Arson', 
        'Rec. Stol. Property', 'Extortion/Blackmail', 'Burglary'
    ],
    'Traffic Related Crimes': [
        'Auto Theft', 'Hit and Run', 'OUI', 'Larceny of Bicycle', 'Larceny of Plate', 
        'Accident', 'Taxi Violation'
    ],
    'Harassment Crimes': [
        'Harassment', 'Indecent Exposure', 'Violation of R.O.', 
        'Violation of H.O.', 'Threats', 'Peeping & Spying', 
        'Sex Offender Violation', 'Stalking', 'Annoying & Accosting'
    ],
    'Public Disorder': [
        'Disorderly', 'Drinking in Public', 'Noise Complaint', 'Annoying & Accosting'
    ],
    'Drugs and Related Crimes': [
        'Drugs', 'Liquor Possession/Sale', 'Drinking in Public', 'OUI'
    ],
    'Prostitution Related Crimes': [
        'Prostitution', 'Sex Offender Violation', 'Indecent Exposure'
    ],
    'Warrant Related Crimes': [
        'Warrant Arrest', 'Disorderly', 'Violation of R.O.', 
        'Violation of H.O.', 'Stalking', 'Domestic Dispute'
    ],
    'Misc. Crimes': [
        'Phone Calls', 'Missing Person', 'Suspicious Package'
    ]

    
}

# Define color mapping directly for each category and crime type
COLOR_MAP = {
    # Larceny Crimes
    'Larceny (Misc)': '#1f77b4',  # muted blue
    'Larceny from Building': '#ff7f0e',  # safety orange
    'Larceny from MV': '#2ca02c',  # cooked asparagus green
    'Larceny from Person': '#d62728',  # brick red
    'Larceny from Residence': '#9467bd',  # muted purple
    'Larceny of Bicycle': '#8c564b',  # chestnut brown
    'Larceny of Plate': '#e377c2',  # raspberry yogurt pink
    'Larceny of Services': '#7f7f7f',  # middle gray

    # Fraud And Financial Crimes
    'Forgery': '#1f77b4',  # muted blue
    'Counterfeiting': '#ff7f0e',  # safety orange
    'Embezzlement': '#2ca02c',  # cooked asparagus green
    'Flim Flam': '#d62728',  # brick red
    'Larceny of Services': '#9467bd',  # muted purple
    'Gambling': '#8c564b',  # chestnut brown

    # Violent Crimes
    'Aggravated Assault': '#1f77b4',  # muted blue
    'Simple Assault': '#ff7f0e',  # safety orange
    'Homicide': '#2ca02c',  # cooked asparagus green
    'Kidnapping': '#d62728',  # brick red
    'Street Robbery': '#9467bd',  # muted purple
    'Commercial Robbery': '#8c564b',  # chestnut brown
    'Domestic Dispute': '#e377c2',  # raspberry yogurt pink
    'Weapon Violations': '#7f7f7f',  # middle gray

    # Property Crimes
    'Commercial Break': '#1f77b4',  # muted blue
    'Housebreak': '#ff7f0e',  # safety orange
    'Mal. Dest. Property': '#2ca02c',  # cooked asparagus green
    'Arson': '#d62728',  # brick red
    'Rec. Stol. Property': '#9467bd',  # muted purple
    'Extortion/Blackmail': '#8c564b',  # chestnut brown
    'Burglary': '#e377c2',  # raspberry yogurt pink

    # Traffic Related Crimes
    'Auto Theft': '#1f77b4',  # muted blue
    'Hit and Run': '#ff7f0e',  # safety orange
    'OUI': '#2ca02c',  # cooked asparagus green
    'Larceny of Bicycle': '#d62728',  # brick red
    'Larceny of Plate': '#9467bd',  # muted purple
    'Accident': '#8c564b',  # chestnut brown
    'Taxi Violation': '#e377c2',  # raspberry yogurt pink

    # Harassment Crimes
    'Harassment': '#1f77b4',  # muted blue
    'Indecent Exposure': '#ff7f0e',  # safety orange
    'Violation of R.O.': '#2ca02c',  # cooked asparagus green
    'Violation of H.O.': '#d62728',  # brick red
    'Threats': '#9467bd',  # muted purple
    'Peeping & Spying': '#8c564b',  # chestnut brown
    'Sex Offender Violation': '#e377c2',  # raspberry yogurt pink
    'Stalking': '#7f7f7f',  # middle gray
    'Annoying & Accosting': '#bcbd22',  # curry yellow-green

    # Public Disorder
    'Disorderly': '#1f77b4',  # muted blue
    'Drinking in Public': '#ff7f0e',  # safety orange
    'Noise Complaint': '#2ca02c',  # cooked asparagus green
    'Annoying & Accosting': '#d62728',  # brick red

    # Drugs and Related Crimes
    'Drugs': '#1f77b4',  # muted blue
    'Liquor Possession/Sale': '#ff7f0e',  # safety orange
    'Drinking in Public': '#2ca02c',  # cooked asparagus green
    'OUI': '#d62728',  # brick red

    # Prostitution Related Crimes
    'Prostitution': '#1f77b4',  # muted blue
    'Sex Offender Violation': '#ff7f0e',  # safety orange
    'Indecent Exposure': '#2ca02c',  # cooked asparagus green

    # Warrant Related Crimes
    'Warrant Arrest': '#1f77b4',  # muted blue
    'Disorderly': '#ff7f0e',  # safety orange
    'Violation of R.O.': '#2ca02c',  # cooked asparagus green
    'Violation of H.O.': '#d62728',  # brick red
    'Stalking': '#9467bd',  # muted purple
    'Domestic Dispute': '#8c564b',  # chestnut brown

    # Misc. Crimes
    'Phone Calls': '#1f77b4',  # muted blue
    'Missing Person': '#ff7f0e',  # safety orange
    'Suspicious Package': '#2ca02c'  # cooked asparagus green
}
