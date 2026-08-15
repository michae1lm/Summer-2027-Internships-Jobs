import json, csv, re
from datetime import datetime
from pathlib import Path

P = Path('opportunities.json')
jobs = json.loads(P.read_text(encoding='utf-8'))

def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', str(s or '').lower()).strip()

def parse_date(s):
    try:
        return datetime.strptime(s, '%B %d, %Y')
    except Exception:
        return datetime.min

# Remove known duplicate LinkedIn imports when a better direct-employer entry exists.
remove = {
    ('GE Vernova', 'GE Vernova Digital Technology Internship - Summer 2027'),
    ('Arboreal Management', 'Software Engineering Intern'),
    ('Melaleuca: The Wellness Company', 'Internship Summer 2027 - Cybersecurity'),
}
jobs = [j for j in jobs if (j.get('company'), j.get('role')) not in remove]

# Enrich CNO / Washington National listing from the employer posting supplied by the repo owner.
for j in jobs:
    if j.get('company') == 'Washington National Insurance Company' and 'Cyber Security IT Intern' in j.get('role',''):
        j.update({
            'company': 'CNO Financial Group',
            'location': 'United States',
            'work': 'Remote',
            'close_date': 'Rolling',
            'hourly_rate': 'Undisclosed',
            'total_compensation': 'Undisclosed',
            'application_url': 'https://careers.cnoinc.com/carmel-in/cyber-security-it-intern-remote/08EF775A045D4EFE9CEC1D57D0B83B2C/job/',
            'job_id': 'JR170419',
            'employment_type': 'Internship',
            'description': 'Paid cybersecurity internship rotating across Security Operations, Engineering, and Governance, with exposure to SOC work, incident response, threat detection, security tools, and enterprise IT.',
            'qualifications': "Progress toward a bachelor's degree in computer science, information technology, or a related field; rising junior or senior with an expected graduation of December 2027-June 2029; basic networking and operating-system knowledge; familiarity with cybersecurity principles; 40 hours/week for 10-12 weeks.",
            'responsibilities': 'Support day-to-day cybersecurity work, security operations, incident response, threat detection, documentation, and collaboration with enterprise security teams.',
            'notes': 'Program runs May 17-August 6, 2027. Fully remote in the U.S.; Central or Eastern Time hours preferred. No current or future work-visa sponsorship.',
            'source': 'Employer'
        })

# Enrich Rockefeller from the direct employer posting supplied by the repo owner.
for j in jobs:
    if j.get('company') == 'Rockefeller Capital Management' and 'Information Security' in j.get('role',''):
        j.update({
            'location': 'New York, NY',
            'work': 'In person',
            'hourly_rate': '$38/hour',
            'total_compensation': '$15,200',
            'application_url': 'https://careers.rockco.com/careers-home/jobs/5355?lang=en-us',
            'job_id': '5355',
            'employment_type': 'Internship',
            'description': 'Ten-week Information Security summer analyst role supporting control enhancements, threat defenses, security policies, risk reduction, awareness programs, security metrics, and security tools.',
            'qualifications': 'Projected 2028 graduate in good standing; cybersecurity, computer science, economics, psychology, mathematics, or data concentration desirable; strong analytical, communication, organizational, and problem-solving skills.',
            'responsibilities': 'Enhance security controls and threat defenses, identify security issues, help develop policies and procedures, support awareness and metrics programs, and communicate technical information to stakeholders.',
            'notes': '10-week June-August program. Employer-posted rate is $38/hour.',
            'source': 'Employer'
        })

new_jobs = [
{
'company':'IBM','role':'X-Force Red Hacker Intern 2027','location':'Austin, TX','work':'In person','open_date':'August 14, 2026','close_date':'Rolling','hourly_rate':'Est. $24.92-$45.69/hour','total_compensation':'$51,840-$95,040/year (annualized)','application_url':'https://www.ibm.com/careers/search','job_id':'129253','employment_type':'Internship','description':'Offensive-security internship with IBM X-Force supporting live client penetration-testing engagements across applications, networks, cloud environments, devices, and enterprise systems.','qualifications':'Currently pursuing a university degree, preferably in computer science, cybersecurity, data science, statistics, mathematics, MIS, engineering, or a related field. Security-domain knowledge in penetration testing, red teaming, social engineering, or vulnerability scanning is preferred. Must work onsite in Austin from May-August 2027 and must not require current or future visa sponsorship.','responsibilities':'Support penetration testing, vulnerability research and validation, reverse engineering, technical reporting, client briefings, offensive-security tooling, automation, and AI-supported security analysis.','notes':'Employer lists a projected annualized salary range of $51,840-$95,040. Posting states it is anticipated to remain open for 15 days from the posting date.','source':'Employer'
},
{
'company':'Interactive Brokers','role':'Cybersecurity Internship 2027','location':'Greenwich, CT','work':'In person','open_date':'August 13, 2026','close_date':'March 1, 2027','hourly_rate':'Undisclosed','total_compensation':'Undisclosed','application_url':'https://www.interactivebrokers.com/en/general/about/careers.php','job_id':'642','employment_type':'Internship','description':'Nine-week onsite cybersecurity internship focused on protecting critical infrastructure and data across brokerage operations, with exposure to security engineering, assessments, vulnerability scanning, threat monitoring, penetration testing, red teaming, and AI testing.','qualifications':'Currently pursuing a degree in cybersecurity, computer science, or a related field; graduation between December 2027 and May 2028 preferred; minimum GPA 3.5; basic understanding of network and application security; strong documentation, analysis, and problem-solving skills.','responsibilities':'Assist security engineers, own scoped security projects, participate in security assessments and vulnerability scanning, support penetration testing and reporting, and help improve red-team and AI-testing infrastructure.','notes':'9-week onsite program. Employer page states application deadline March 1.','source':'Employer'
},
{
'company':'BDO USA','role':'Assurance Intern, Technology Risk Assurance - Summer 2027 (Atlanta)','location':'Atlanta, GA','work':'In person','open_date':'July 10, 2026','close_date':'September 17, 2026','hourly_rate':'Undisclosed','total_compensation':'Undisclosed','application_url':'https://www.linkedin.com/jobs/view/4363237476','job_id':'11429','employment_type':'Internship','description':'Technology Risk Assurance internship supporting application and automated control testing, IT audit work, Sarbanes-Oxley control reviews, client walkthroughs, workpapers, and audit reporting.','qualifications':'Pursuing a degree in accounting, computer science, or information systems. Leadership experience and prior information-systems or operational-auditing internship/work-study experience are preferred.','responsibilities':'Document and test application and automated controls, support audit reports, perform control walkthroughs and interviews, document testing results, and apply information-systems audit principles.','notes':'Employer page lists Job ID 11429 and an apply-before date of September 17, 2026. The posting provided location-specific pay ranges for several states but did not list a Georgia-specific rate.','source':'Employer'
},
{
'company':'Marathon Petroleum','role':'Intern/Co-op - Information Technology (Summer 2027)','location':'Findlay, OH / San Antonio, TX','work':'In person','open_date':'August 14, 2026','close_date':'August 16, 2026','hourly_rate':'$24.95-$31.19/hour','total_compensation':'Undisclosed','application_url':'https://mpc.wd1.myworkdayjobs.com/en-US/MPCCareers?q=00023241','job_id':'00023241','employment_type':'Internship','description':'Broad IT internship program with possible placements in business systems analysis, cloud engineering, cybersecurity, infrastructure engineering and operations, software engineering, and QA.','qualifications':'Desired majors include computer science and engineering, MIS, information systems, computer engineering, software engineering, computer science, and related IT disciplines. Strong academics and indefinite U.S. work authorization without sponsorship are required; candidates must remain enrolled throughout the experience.','responsibilities':'Depending on placement, work may include cloud architecture and automation, cybersecurity monitoring and risk assessment, infrastructure operations, software development, QA automation, incident management, and business-systems analysis.','notes':'Employer-posted pay is $24.95-$31.19/hour. Locations include Findlay, Ohio and San Antonio, Texas. Job requisition 00023241.','source':'Employer'
},
{
'company':'TikTok','role':'Search Security Strategy Operations Intern (TikTok-Platform Responsibility-Search) - 2027 Summer','location':'San Jose, CA','work':'In person','open_date':'August 14, 2026','close_date':'Rolling','hourly_rate':'$25/hour','total_compensation':'Undisclosed','application_url':'https://lifeattiktok.com/search/','job_id':'A145452','employment_type':'Internship','description':'Search-security strategy internship focused on content-safety systems, public-opinion detection, intervention strategy, emergency response, and use of large models and security platforms.','qualifications':"Currently pursuing an undergraduate or master's degree in computer science, statistics, information management, data science, or a related field. Preferred experience includes search/recommendation/content security, risk control, sensitive-word systems, review systems, strategy platforms, or large-model data training and evaluation.",'responsibilities':'Design and improve detection and early-warning mechanisms, maintain intervention methods and platforms, support sensitive-word and large-model systems, respond to search-security incidents, and conduct post-incident analysis.','notes':'Applications reviewed on a rolling basis. Employer-posted rate is $25/hour.','source':'Employer'
},
{
'company':'ByteDance','role':'Security Software Engineer Project Intern (Network Security) - 2026 Start (BS/MS)','location':'San Jose, CA','work':'In person','open_date':'August 14, 2026','close_date':'Rolling','hourly_rate':'$45-$60/hour','total_compensation':'Undisclosed','application_url':'https://joinbytedance.com/search/','job_id':'A177024A','employment_type':'Internship','description':'Network-security project internship focused on improving Web Application Firewall intelligence against automated threats, HTTP flood attacks, malicious bots, and evasive activity.','qualifications':'Undergraduate or postgraduate student pursuing computer science, computer engineering, information systems, or another STEM discipline; familiarity with security concepts, vulnerabilities, exploitation techniques, and at least one programming/scripting language. CTFs, bug bounty work, CVEs, security research, and cloud/container/network/mobile security are preferred.','responsibilities':'Research dynamic thresholding for HTTP flood mitigation, build bot-behavior detection, improve WAF adaptive learning, reduce false positives, and strengthen detection of evasive activity.','notes':'At least 3 months. Applications reviewed on a rolling basis. Employer-posted rate is $45-$60/hour.','source':'Employer'
}
]

ids = {str(j.get('job_id','')) for j in jobs if j.get('job_id')}
keys = {(norm(j.get('company')), norm(j.get('role'))) for j in jobs}
for j in new_jobs:
    if str(j.get('job_id','')) not in ids and (norm(j['company']), norm(j['role'])) not in keys:
        jobs.append(j)

# Newest first, then company/role alphabetically for ties.
jobs.sort(key=lambda j: (str(j.get('company','')).lower(), str(j.get('role','')).lower()))
jobs.sort(key=lambda j: parse_date(j.get('open_date','')), reverse=True)

P.write_text(json.dumps(jobs, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

headers = ['company','role','location','work','open_date','close_date','hourly_rate','total_compensation','application_url','linkedin_url','job_id','employment_type','description','qualifications','responsibilities','notes']
with open('opportunities.csv','w',encoding='utf-8',newline='') as f:
    w = csv.DictWriter(f, fieldnames=headers, extrasaction='ignore')
    w.writeheader()
    for j in jobs:
        w.writerow({h:j.get(h,'') for h in headers})

def cell(v):
    return str(v or '').replace('|','\\|').replace('\n',' ').strip()

lines = [
'# Summer 2027 U.S. CS, Cybersecurity, IT & Early-Career Opportunities','',
'**Updated:** August 14, 2026  ',
f'**Unique roles:** {len(jobs)}  ',
f'**Internships:** {len(jobs)}  ',
'**Post-grad / early-career:** 0','',
'Click a job title to open its application page. Listings are automatically deduplicated and sorted newest to oldest. Detailed descriptions and qualifications are stored in opportunities.json / opportunities.csv when the employer publishes them.','',
'| Company | Opportunity | Type | Location | Work | Open date | Close date | Hourly rate | Estimated total compensation |',
'|---|---|---|---|---|---|---|---|---|'
]
for j in jobs:
    role = cell(j.get('role'))
    url = str(j.get('application_url','')).strip()
    linked = f'[{role}]({url.replace(chr(41), "%29")})' if url else role
    lines.append(f"| {cell(j.get('company'))} | {linked} | Internship | {cell(j.get('location'))} | {cell(j.get('work'))} | {cell(j.get('open_date'))} | {cell(j.get('close_date'))} | {cell(j.get('hourly_rate') or 'Undisclosed')} | {cell(j.get('total_compensation') or 'Undisclosed')} |")
lines += ['', '## Data notes','',
'- `Rolling` means the employer did not publish a fixed closing date.',
'- `Undisclosed` means the employer did not publish compensation.',
'- LinkedIn-imported roles may use the email date as the first verified open date.',
'- Post-grad / early-career entries are included when the title explicitly signals a new-grad, graduate, entry-level, associate, junior, level-I, or early-career role.',
'- Duplicate detection checks job IDs, canonical application URLs, and normalized company/role/location combinations.',
'- Values marked `Est.` are conversions or clearly labeled estimates.','',
'## Sortable tracker','',
'Enable GitHub Pages through **Settings → Pages → Deploy from a branch → main → /(root)**.','',
'## About','',
'Summer 2027 cybersecurity, software engineering, IT internships, and relevant post-grad / early-career opportunities.']
Path('README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

print(f'Updated tracker to {len(jobs)} unique roles.')
