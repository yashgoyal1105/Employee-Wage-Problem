import random

class EmployeeWage:
    """Class to compute employee wages for multiple companies with different parameters."""
    
    @classmethod
    def get_work_hours(cls):
        """Returns random work hours (0 for absent, 4 for part-time, 8 for full-time)."""
        return random.choice([0, 4, 8])

    @classmethod
    def calculate_daily_wage(cls, per_hour_wage):
        """Calculates daily wage based on work hours and returns wage, status, and hours worked."""
        work_hours = cls.get_work_hours()
        
        match work_hours:
            case 0:
                daily_wage = 0
                attendance_status = "Absent"
            case 4:
                daily_wage = per_hour_wage * 4
                attendance_status = "Part-time"
            case 8:
                daily_wage = per_hour_wage * 8
                attendance_status = "Full-time"
        
        return daily_wage, attendance_status, work_hours
    
    @classmethod
    def calculate_monthly_wage(cls, per_hour_wage, working_days_per_month):
        """Calculates and returns total wage for a month based on working days."""
        total_wage = 0
        for _ in range(working_days_per_month):
            daily_wage, _, _ = cls.calculate_daily_wage(per_hour_wage)
            total_wage += daily_wage
        return total_wage
    
    @classmethod
    def calculate_wage_with_condition(cls, per_hour_wage, working_days_per_month, max_work_hours):
        """Calculates total wage considering max work hours and max working days."""
        total_wage = 0
        total_work_hours = 0
        total_working_days = 0
        
        while total_work_hours < max_work_hours and total_working_days < working_days_per_month:
            daily_wage, _, work_hours = cls.calculate_daily_wage(per_hour_wage)
            total_wage += daily_wage
            total_work_hours += work_hours
            total_working_days += 1
        
        return total_wage, total_work_hours, total_working_days

print("Welcome to Employee Wage Computation Program")

# Example computation for multiple companies
companies = [
    {"name": "Company A", "per_hour_wage": 20, "working_days": 20, "max_hours": 100},
    {"name": "Company B", "per_hour_wage": 25, "working_days": 22, "max_hours": 110}
]

for company in companies:
    print(f"\nCalculating wages for {company['name']}")
    daily_wage, attendance_status, _ = EmployeeWage.calculate_daily_wage(company['per_hour_wage'])
    monthly_wage = EmployeeWage.calculate_monthly_wage(company['per_hour_wage'], company['working_days'])
    total_wage, total_hours, total_days = EmployeeWage.calculate_wage_with_condition(
        company['per_hour_wage'], company['working_days'], company['max_hours']
    )

    print(f"Employee is {attendance_status}")
    print(f"Daily Wage: ₹{daily_wage}")
    print(f"Total Monthly Wage: ₹{monthly_wage}")
    print(f"Total Wage till condition met: ₹{total_wage}")
    print(f"Total Work Hours: {total_hours}")
    print(f"Total Working Days: {total_days}")
