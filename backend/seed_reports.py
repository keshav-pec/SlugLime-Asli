from app import create_app
from models import Report
from security import gen_ticket_id, gen_access_code, hash_code
from database import db

app = create_app()

with app.app_context():
    # Check if reports exist
    count = Report.query.count()
    print(f"Current reports in database: {count}")
    
    if count < 5:
        # Create sample reports
        reports_data = [
            {
                "title": "Financial Irregularities in Procurement Department",
                "category": "corruption",
                "body": "I've noticed suspicious patterns in the procurement process. Multiple contracts worth millions have been awarded to the same vendor without proper competitive bidding. Invoice amounts seem inflated compared to market rates. This needs immediate investigation."
            },
            {
                "title": "Safety Violations at Manufacturing Plant",
                "category": "safety",
                "body": "The facility has been operating with expired safety certifications for over 6 months. Management is aware but refuses to address it. Multiple near-miss incidents have been reported but not logged properly. Workers are at risk."
            },
            {
                "title": "Data Privacy Breach - Customer Information Exposed",
                "category": "fraud",
                "body": "Customer database containing personal information was left publicly accessible on an unsecured server for several weeks. This affects approximately 50,000 users. The incident was discovered but not reported to authorities as required by law."
            },
            {
                "title": "Workplace Harassment Cover-up by HR",
                "category": "harassment",
                "body": "Multiple employees have filed complaints about inappropriate behavior by a senior manager. HR has been dismissing these complaints and pressuring victims to withdraw their statements. This pattern has been ongoing for over a year and creates a hostile work environment."
            },
            {
                "title": "Environmental Violations and Illegal Waste Disposal",
                "category": "other",
                "body": "The company has been disposing of hazardous waste illegally to avoid proper disposal costs. This includes dumping chemicals in unauthorized areas. Environmental regulations are being systematically violated with management's knowledge."
            }
        ]
        
        for data in reports_data:
            ticket = gen_ticket_id()
            code = gen_access_code()
            
            report = Report(
                ticket=ticket,
                title=data["title"],
                category=data["category"],
                body=data["body"],
                code_hash=hash_code(code),
                status="open"
            )
            db.session.add(report)
        
        db.session.commit()
        print(f"✅ Created {len(reports_data)} sample reports")
    else:
        print("✅ Sample reports already exist")
    
    print(f"✅ Total reports in database: {Report.query.count()}")
