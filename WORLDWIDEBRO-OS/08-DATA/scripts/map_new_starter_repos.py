import json, csv, re, os
from pathlib import Path

ROOT = Path('/Users/acebless/Documents/WORLDWIDEBRO-OS')
REG = ROOT / '08-DATA' / 'registries'
PILOT = ROOT / 'REGISTRIES' / 'repository_registry_pilot.json'

CAPABILITIES = [
    'api','database','authentication','dashboard','monitoring','portfolio','security',
    'workspace','graph','payments','llm','agent','mcp','rag','search','scheduling',
    'notifications','ocr','crm','analytics','machine-learning','automation','devtools',
    'construction','fashion-design'
]

SECTOR_ALIASES = {
    'ecommerce/marketplace': ['e-commerce','marketplace','shop','store','product'],
    'social-media/communication': ['social','chat','messaging','communication','discord','slack','whatsapp'],
    'education/lms': ['education','lms','learning','course','quiz'],
    'media/entertainment': ['media','video','music','spotify','netflix','podcast','conference'],
    'booking/reservations': ['booking','reservation','hotel','airbnb','ticket','flight'],
    'productivity/project-management': ['productivity','project','task','calendar','kanban','notes'],
    'food-delivery': ['food','delivery','meal','recipe','restaurant'],
    'finance/payments': ['finance','banking','expense','budget','stock','crypto','invoice','payment'],
    'healthcare/fitness': ['healthcare','hospital','fitness','patient','pharmacy','telemedicine'],
    'email/messaging': ['email','newsletter','sms'],
    'inventory/crm': ['inventory','warehouse','pos','crm'],
    'mobile-first': ['pwa','weather','news','job'],
    'creative/design': ['portfolio','photo','design','meme','figma'],
    'analytics/dashboards': ['dashboard','analytics','bi','visualization'],
    'auth/security': ['auth','password','2fa','totp'],
    'ai/ml': ['ai','ml','chatbot','sentiment','recommendation','image'],
    'maps/location': ['map','location','route','delivery'],
    'cms/wiki/forum/docs': ['cms','wiki','forum','documentation','reddit'],
    'developer-tools': ['developer','snippet','api testing','url','devops'],
}

NEW_REPOS = [
    # E-Commerce & Marketplace
    ("amazona","https://github.com/basir/amazona","mern-stack-amazon-clone","e-commerce"),
    ("nulti-venc'or-ecommerce","https://github.com/6pm-tech/nulti-venc'or-ecommerce","multi-vendor marketplace","e-commerce"),
    ("bookstore-mern","https://github.com/DarkSoul26/bookstore-mern","online bookstore","e-commerce"),
    ("E-commerce-site","https://github.com/mithlesh-bit/E-commerce-site","fashion store with AR try-on","e-commerce"),
    ("grocery-app","https://github.com/shakyShane/grocery-app","grocery delivery app","food-delivery"),
    # Social Media & Communication
    ("project_mern_memories","https://github.com/adrianhajdin/project_mern_memories","facebook clone","social-media/communication"),
    ("next13-social-app","https://github.com/safak/youtube/tree/mern-social-app","social media app clone","social-media/communication"),
    ("twitter-clone","https://github.com/ooloth/twitter-clone","twitter clone","social-media/communication"),
    ("linkedin-clone","https://github.com/CleverProgrammers/linkedin-clone","linkedin clone","social-media/communication"),
    ("project_chat_application","https://github.com/adrianhajdin/project_chat_application","realtime chat","social-media/communication"),
    ("next13-discord-clone","https://github.com/antonioerdeljac/next13-discord-clone","discord clone","social-media/communication"),
    ("whatsapp-mern","https://github.com/CleverProgrammers/whatsapp-mern","whatsapp clone","social-media/communication"),
    ("slack-clone-client","https://github.com/pusher/slack-clone-client","slack clone","social-media/communication"),
    # Learning Management Systems
    ("next13-1ms-platform","https://github.com/antonioerdeljac/next13-1ms-platform","lms platform","education/lms"),
    ("MERN-Stack-Course","https://github.com/PacktPublishing/MERN-Stack-Course","online course platform","education/lms"),
    ("student-management-system","https://github.com/mkkhedawat/student-management-system","student portal","education/lms"),
    ("quiz-app","https://github.com/safak/youtube/tree/quiz-app","quiz application","education/lms"),
    # Media & Entertainment
    ("netflix-clone","https://github.com/karlhadwen/netflix-clone","netflix clone","media/entertainment"),
    ("youtube-clone","https://github.com/manikandanraji/youtube-clone","youtube clone","media/entertainment"),
    ("spotify-clone-client","https://github.com/JL978/spotify-clone-client","spotify clone","media/entertainment"),
    ("mini-player","https://github.com/muhammederdem/mini-player","music streaming app","media/entertainment"),
    ("zoom-clone","https://github.com/CleverProgrammers/zoom-clone","video conferencing","media/entertainment"),
    ("realworld","https://github.com/gothinkster/realworld","realworld medium clone","media/entertainment"),
    ("podcast-app","https://github.com/johndoe/podcast-app","podcast platform","media/entertainment"),
    # Booking & Reservations
    ("hotel-management-full-stack","https://github.com/machadop1407/hotel-management-full-stack","hotel booking","booking/reservations"),
    ("airbnb-clone","https://github.com/safak/youtube/tree/airbnb-clone","airbnb clone","booking/reservations"),
    ("restaurant-reservation","https://github.com/mikhael28/restaurant-reservation","restaurant reservation","booking/reservations"),
    ("online-movie-ticket-booking-syste","https://github.com/isuruAb/online-movie-ticket-booking-syste","movie ticket booking","booking/reservations"),
    ("flight-booking-system","https://github.com/coding-dojo-sndip/flight-booking-system","flight booking","booking/reservations"),
    # Productivity & Project Management
    ("trello-clone","https://github.com/reedbarger/trello-clone","trello clone","productivity/project-management"),
    ("notion-clone","https://github.com/konstantinmuenster/notion-clone","notion clone","productivity/project-management"),
    ("jira_clone","https://github.com/oldboyxx/jira_clone","jira clone","productivity/project-management"),
    ("mern-todo","https://github.com/CleverProgrammers/mern-todo","task management app","productivity/project-management"),
    ("calendso","https://github.com/calendso/calendso","calendar scheduling app","productivity/project-management"),
    ("react-trello","https://github.com/rcdexta/react-trello","kanban board","productivity/project-management"),
    ("note-taking-app","https://github.com/FaisalST32/note-taking-app","note taking app","productivity/project-management"),
    # Food & Delivery
    ("foodordering-mernstack","https://github.com/shakyShane/foodordering-mernstack","uber eats clone","food-delivery"),
    ("recipe-site","https://github.com/machadop1487/recipe-site","recipe sharing","food-delivery"),
    ("restaurant-webapp","https://github.com/ipenywis/restaurant-webapp","restaurant menu","food-delivery"),
    ("meal-planner","https://github.com/chingu-voyages/v25-geckos-team-85","meal planner","food-delivery"),
    # Finance & Payments
    ("Banking-Application","https://github.com/TannerGabriel/Banking-Application","banking app","finance/payments"),
    ("Expense-Tracker-Fullstack","https://github.com/machadop1487/Expense-Tracker-Fullstack","expense tracker","finance/payments"),
    ("project_cryptoverse","https://github.com/adrianhajdin/project_cryptoverse","cryptocurrency dashboard","finance/payments"),
    ("invoiceninja","https://github.com/invoiceninja/invoiceninja","invoice management","finance/payments"),
    ("awesome-react","https://github.com/enaqx/awesome-react","awesome-react","finance/payments"),
    ("awesome-stock-resources","https://github.com/prathyvsh/awesome-stock-resources","stock portfolio","finance/payments"),
    # Healthcare & Fitness
    ("Hospital-Management-System","https://github.com/shubhammehra4/Hospital-Management-System","hospital management","healthcare/fitness"),
    ("telemedicine-platform","https://github.com/simple-online-healthcare/telemedicine-platform","telemedicine platform","healthcare/fitness"),
    ("pharmacy-management-system","https://github.com/shuvooa787/pharmacy-management-system","pharmacy management","healthcare/fitness"),
    # Email & Messaging
    ("gmail-clone","https://github.com/CleverProgrammers/gmail-clone","gmail clone","email/messaging"),
    ("Ghost","https://github.com/TryGhost/Ghost","newsletter platform","email/messaging"),
    ("plivo-examples-node","https://github.com/plivo/plivo-examples-node","sms marketing","email/messaging"),
    # Inventory & CRM
    ("inventory-management-system","https://github.com/saadpasta/inventory-management-system","inventory management","inventory/crm"),
    ("corteza-server","https://github.com/cortezeproject/corteza-server","crm application","inventory/crm"),
    ("wms","https://github.com/warehouse-management-system/wms","warehouse management","inventory/crm"),
    ("POS-System","https://github.com/loystar/POS-System","point of sale","inventory/crm"),
    # Mobile-First Applications
    ("pwa-starter-kit","https://github.com/GoogleChromeLabs/pwa-starter-kit","pwa starter","mobile-first"),
    ("project_weather_app","https://github.com/adrianhajdin/project_weather_app","weather app","mobile-first"),
    ("News-App-Full-Stack","https://github.com/machadop1407/News-App-Full-Stack","news aggregator","mobile-first"),
    ("job-beard","https://github.com/safak/youtube/tree/job-beard","job board","mobile-first"),
    # Creative & Design
    ("gatsby-simplefolio","https://github.com/cobidev/gatsby-simplefolio","portfolio builder","creative/design"),
    ("tldraw","https://github.com/tldraw/tldraw","design collaboration","creative/design"),
    ("Meme_Api","https://github.com/R313nt13ss/Meme_Api","meme generator","creative/design"),
    # Analytics & Dashboards
    ("sing-app-react","https://github.com/flatlogic/sing-app-react","admin dashboard","analytics/dashboards"),
    ("keen-js","https://github.com/keen/keen-js","analytics platform","analytics/dashboards"),
    ("superset","https://github.com/apache/superset","data visualization dashboard","analytics/dashboards"),
    ("metabase","https://github.com/metabase/metabase","business intelligence tool","analytics/dashboards"),
    # Authentication & Security
    ("hackathon-starter","https://github.com/sahat/hackathon-starter","auth system","auth/security"),
    ("server","https://github.com/bitwarden/server","password manager","auth/security"),
    ("google-authenticator","https://github.com/google/google-authenticator","two-factor auth","auth/security"),
    # AI & Machine Learning
    ("botpress","https://github.com/botpress/botpress","chatbot platform","ai/ml"),
    ("tfjs-examples","https://github.com/tensorflow/tfjs-examples","image recognition app","ai/ml"),
    ("Surprise","https://github.com/NicolasHug/Surprise","recommendation system","ai/ml"),
    ("sentiment","https://github.com/vivekn/sentiment","sentiment analysis tool","ai/ml"),
    # Maps & Location
    ("project_travel_companion","https://github.com/adrianhajdin/project_travel_companion","location based service","maps/location"),
    ("kepler.gl","https://github.com/uber/kepler.gl","map visualization tool","maps/location"),
    ("vroom","https://github.com/VR00M-Project/vroom","delivery route optimizer","maps/location"),
    # Content Management
    ("strapi","https://github.com/strapi/strapi","cms platform","cms/wiki/forum/docs"),
    ("wiki","https://github.com/Requarks/wiki","wiki system","cms/wiki/forum/docs"),
    ("reddit-clone-mern-stack","https://github.com/levblanc/reddit-clone-mern-stack","forum platform","cms/wiki/forum/docs"),
    ("docusaurus","https://github.com/facebook/docusaurus","documentation platform","cms/wiki/forum/docs"),
    # Developer Tools
    ("massCode","https://github.com/antonreshetov/massCode","code snippet manager","developer-tools"),
    ("hoppscotch","https://github.com/hoppscotch/hoppscotch","api testing tool","developer-tools"),
    ("grafana","https://github.com/grafana/grafana","devops dashboard","developer-tools"),
    ("kutt","https://github.com/thedevs-network/kutt","url shortener","developer-tools"),
]

NAME_HINTS = {
    'amazona': ['e-commerce','shop','product','cart'],
    'E-commerce-site': ['e-commerce','shop','product'],
    'grocery-app': ['grocery','delivery','food'],
    'project_mern_memories': ['social','posts','share'],
    'next13-social-app': ['social','posts','share'],
    'twitter-clone': ['social','tweets','feed'],
    'linkedin-clone': ['professional','jobs','feed'],
    'project_chat_application': ['chat','messaging','realtime'],
    'next13-discord-clone': ['chat','servers','channels'],
    'whatsapp-mern': ['chat','messaging','status'],
    'slack-clone-client': ['chat','channels','workspace'],
    'next13-1ms-platform': ['course','learning','video'],
    'MERN-Stack-Course': ['course','learning','education'],
    'student-management-system': ['student','school','enrollment'],
    'quiz-app': ['quiz','assessment','course'],
    'netflix-clone': ['video','streaming','movies'],
    'youtube-clone': ['video','upload','channel'],
    'spotify-clone-client': ['music','audio','playlists'],
    'mini-player': ['music','audio','player'],
    'zoom-clone': ['video','conference','call'],
    'realworld': ['articles','blog','feed'],
    'podcast-app': ['podcast','audio','episodes'],
    'hotel-management-full-stack': ['hotel','reservation','booking'],
    'airbnb-clone': ['rental','property','booking'],
    'restaurant-reservation': ['restaurant','reservation','table'],
    'online-movie-ticket-booking-syste': ['movie','ticket','booking'],
    'flight-booking-system': ['flight','airline','booking'],
    'trello-clone': ['board','task','lists'],
    'notion-clone': ['notes','database','pages'],
    'jira_clone': ['sprint','issue','project'],
    'mern-todo': ['todo','tasks','projects'],
    'calendso': ['calendar','booking','meeting'],
    'react-trello': ['board','task','kanban'],
    'note-taking-app': ['notes','notebook','editor'],
    'foodordering-mernstack': ['food','order','delivery'],
    'recipe-site': ['recipe','food','ingredients'],
    'restaurant-webapp': ['restaurant','menu','order'],
    'meal-planner': ['meal','plan','grocery'],
    'Banking-Application': ['banking','account','transfer'],
    'Expense-Tracker-Fullstack': ['expense','budget','transaction'],
    'project_cryptoverse': ['crypto','dashboard','price'],
    'invoiceninja': ['invoice','billing','client'],
    'awesome-react': ['react','components','examples'],
    'awesome-stock-resources': ['stock','market','portfolio'],
    'Hospital-Management-System': ['hospital','patient','doctor'],
    'telemedicine-platform': ['doctor','patient','video'],
    'pharmacy-management-system': ['pharmacy','medicine','prescription'],
    'gmail-clone': ['email','inbox','compose'],
    'Ghost': ['newsletter','blog','email'],
    'plivo-examples-node': ['sms','message','campaign'],
    'inventory-management-system': ['inventory','warehouse','stock'],
    'corteza-server': ['crm','contacts','deals'],
    'wms': ['warehouse','inventory','picker'],
    'POS-System': ['pos','sales','checkout'],
    'pwa-starter-kit': ['pwa','mobile','offline'],
    'project_weather_app': ['weather','forecast','location'],
    'News-App-Full-Stack': ['news','headlines','feed'],
    'job-beard': ['jobs','board','applications'],
    'gatsby-simplefolio': ['portfolio','resume','projects'],
    'tldraw': ['drawing','collaboration','canvas'],
    'Meme_Api': ['meme','image','share'],
    'sing-app-react': ['dashboard','admin','charts'],
    'keen-js': ['analytics','events','charts'],
    'superset': ['dashboard','bi','charts'],
    'metabase': ['bi','charts','dashboard'],
    'hackathon-starter': ['auth','login','passport'],
    'server': ['vault','password','security'],
    'google-authenticator': ['2fa','totp','security'],
    'botpress': ['chatbot','flows','nlp'],
    'tfjs-examples': ['image','model','tensorflow'],
    'Surprise': ['recommendation','matrix','ml'],
    'sentiment': ['sentiment','nlp','text'],
    'project_travel_companion': ['map','location','travel'],
    'kepler.gl': ['visualization','map','data'],
    'vroom': ['route','optimization','fleet'],
    'strapi': ['cms','content','api'],
    'wiki': ['wiki','docs','pages'],
    'reddit-clone-mern-stack': ['forum','posts','votes'],
    'docusaurus': ['docs','pages','markdown'],
    'massCode': ['snippet','code','editor'],
    'hoppscotch': ['api','request','http'],
    'grafana': ['dashboard','metrics','observability'],
    'kutt': ['url','shortener','link'],
}

CAPABILITY_WEIGHTS = {
    'e-commerce/marketplace': ['api','database','authentication','dashboard','payments','security','notifications','search','analytics','automation'],
    'social-media/communication': ['api','database','authentication','dashboard','security','notifications','workspace','search','analytics','mcp','rag'],
    'education/lms': ['api','database','authentication','dashboard','security','video','notifications','search','analytics','llm','mcp'],
    'media/entertainment': ['api','database','authentication','dashboard','security','notifications','search','analytics','llm','mcp','rag'],
    'booking/reservations': ['api','database','authentication','dashboard','payments','notifications','schedule','search','analytics','automation'],
    'productivity/project-management': ['api','database','authentication','dashboard','security','workspace','notifications','search','analytics','mcp','rag'],
    'food-delivery': ['api','database','authentication','dashboard','payments','notifications','search','analytics','automation'],
    'finance/payments': ['api','database','authentication','dashboard','payments','security','analytics','monitoring','mcp','ml'],
    'healthcare/fitness': ['api','database','authentication','dashboard','security','notifications','analytics','llm','ocr','mcp','rag'],
    'email/messaging': ['api','database','authentication','dashboard','security','notifications','analytics','search','llm','mcp'],
    'inventory/crm': ['api','database','authentication','dashboard','security','search','analytics','automation','mcp','ml'],
    'mobile-first': ['api','database','authentication','dashboard','security','notifications','search','analytics'],
    'creative/design': ['api','database','authentication','dashboard','security','workspace','notifications','search','analytics','automation'],
    'analytics/dashboards': ['api','database','authentication','dashboard','security','search','analytics','monitoring','mcp','ml'],
    'auth/security': ['api','database','authentication','dashboard','security','monitoring','notifications','search','analytics','mcp'],
    'ai/ml': ['api','database','authentication','dashboard','security','search','analytics','llm','ml','mcp','rag'],
    'maps/location': ['api','database','authentication','dashboard','security','search','analytics','automation','monitoring'],
    'cms/wiki/forum/docs': ['api','database','authentication','dashboard','security','search','analytics','notifications','workspace'],
    'developer-tools': ['api','database','authentication','dashboard','security','monitoring','search','analytics','automation'],
}

print('loaded pilot', PILOT)
with PILOT.open('r', encoding='utf-8') as f:
    pilot = json.load(f)

existing = {r.get('repo_name') for r in pilot if isinstance(r, dict) and r.get('repo_name')}
print('existing pilot count', len(existing))

def normalize_caps(raw, sector):
    weights = CAPABILITY_WEIGHTS.get(sector, [])
    caps = []
    if sector in {'finance/payments','auth/security'}:
        caps += ['payments','security','authentication']
    elif sector in {'analytics/dashboards'}:
        caps += ['dashboard','analytics']
    elif sector in {'maps/location','inventory/crm'}:
        caps += ['dashboard','analytics']
    elif sector in {'productivity/project-management','cms/wiki/forum/docs','creative/design'}:
        caps += ['dashboard','api']
    elif sector in {'healthcare/fitness','email/messaging','education/lms'}:
        caps += ['dashboard','security','api']
    elif sector in {'media/entertainment','social-media/communication'}:
        caps += ['dashboard','security','api']
    elif sector in {'food-delivery','booking/reservations','e-commerce/marketplace','mobile-first'}:
        caps += ['dashboard','api']
    else:
        caps += ['api','dashboard','database']
    for c in weights:
        if c not in caps:
            caps.append(c)
    # keep canonical only from vocabulary
    caps = [c for c in caps if c in CAPABILITIES]
    caps = list(dict.fromkeys(caps))
    return caps[:8]

added = []
for repo_id, url, purpose, sector in NEW_REPOS:
    if repo_id in existing:
        continue
    caps = normalize_caps(purpose, sector)
    record = {
        'repo_name': repo_id,
        'source': 'starred',
        'url': url,
        'owner': 'third-party-starter',
        'language': 'unknown',
        'stars': 0,
        'category': 'STARTER',
        'venture_studio_role': 'Starter Reference',
        'intelligence_level': 'L1',
        'purpose': purpose,
        'identity_type': 'starter-template',
        'tech_stack': '',
        'os_layers': '',
        'reusability_score': 0,
        'revenue_potential': 0,
        'strategic_value': 0,
        'venture_tier': 'starred',
        'decision_action': 'adopt-or-fork',
        'related_ventures': [],
        'related_repositories': [],
        'graph_edges': [],
        'is_venture_candidate': False,
        'estimated_mrr_k': 0,
        'confidence': 'medium',
        'pilot_flag': True,
        'capabilities': caps,
        'sector': sector
    }
    pilot.append(record)
    existing.add(repo_id)
    added.append((repo_id, sector, caps))

with PILOT.open('w', encoding='utf-8') as f:
    json.dump(pilot, f, indent=2, ensure_ascii=False)
print('added', len(added))
print('new pilot total', len(pilot))
for a in added[:10]:
    print(a)
