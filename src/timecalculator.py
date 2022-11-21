from js import document # type: ignore
import datetime
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 
# Functio showTimeFormDiv will call resetInputValues - function which reset all input values
# 
# After that functio check which clockSystem value user have choisen.
# 
#   if clockSystem value is '12clock', function will display next input but hides othes for valid values
# 
#   if clockSystem value is '24clock', function will hide timeFormatDiv, putting timeFormat first index default value and diplay next three div element, putting 
# 
def showTimeFormDiv(*args):  
    
    resetInputValues(*args)
    
    if clockSystem.value == '12clock':
        timeStartDiv.style.display = 'inline'      # hide start time
        timeForm.style.display = 'inline'       # show am - pm
        weekdayDiv.style.display = 'block'        # hide weekdays
        timeAddedDiv.style.display = 'none'      # hide added time
        
        return
    
    if clockSystem.value == '24clock':
        timeForm.style.display = 'none'         # hide am - pm 
        timeForm.selectedIndex = 0               # set timeFormat dropdown list first index selected (has no value) 
        timeStartDiv.style.display = 'block'     # show start time
        weekdayDiv.style.display = 'block'       # show weekdays
        timeAddedDiv.style.display = 'block'     # show added time
        
        return
        
    
def showTimeDiv(*args):
    
  resetInputValues(*args)  
  timeStartDiv.style.display = 'block'
  weekdayDiv.style.display = 'block'
  timeAddedDiv.style.display = 'block'
    

def resetInputValues(*args):
    warningDiv.textContent = ""
    
    startMinutes.min = '0'
    startMinutes.max = '59'
    startMinutes.value = '0'
    
    weekday.selectedIndex = 0
    
    startHoursAdded.value = '0'
    startMinutesAdded.value = '0'
    
    if clockSystem.value == '12clock':
        startHours.min = '1'
        startHours.max = '12'
        startHours.value = '1'
        return
         
    if clockSystem.value == '24clock':
        timeForm.selectedIndex = 0
        startHours.min = '0'
        startHours.max = '23'
        startHours.value = '0'
        return


def checkValues(*args):
    output = ""
    if clockSystem.value == "":
        output += ' Clock time required'
    else:
        if clockSystem.value == '12clock' and timeForm.value == "":
            output += ' Clock system required'
            
            
        if clockSystem.value == '12clock' and not timeForm.value == "":    
            if 0 > int(str(startHours.value)) < 23 or 0 > int(str(startMinutes.value)) < 59 or 0 > int(str(startHours.value)) < 23 and 0 > int(str(startMinutes.value)) < 59:
                output += ' Starting time required'
            
            if 0 > int(str(startHoursAdded.value)) < 999 or 0 > int(str(startMinutesAdded.value)) < 59 or 0 > int(str(startHoursAdded.value)) < 999 and 0 > int(str(startMinutesAdded.value)) < 59:
                output += ' Added time required'
        
        if clockSystem.value == '24clock':
            
            if 0 > int(str(startHours.value)) < 23 or 0 > int(str(startMinutes.value)) < 59 or 0 > int(str(startHours.value)) < 23 and 0 > int(str(startMinutes.value)) < 59:
                output += ' Starting time required'
            
            if 0 > int(str(startHoursAdded.value)) < 999 or 0 > int(str(startMinutesAdded.value)) < 59 or 0 > int(str(startHoursAdded.value)) < 999 and 0 > int(str(startMinutesAdded.value)) < 59:
                output += ' Added time required'
            
    warningDiv.textContent = output
    
    return warningDiv.textContent == "" or output == ""
       
    
def timefunc(*args):
    
    if checkValues(*args):
        
        new_time = "Clock: "

        clock_system = str(clockSystem.value)
        time_form = str(timeForm.value)
        
        hours = int(str(startHours.value))
        minutes = int(str(startMinutes.value))
        
        week_day = str(weekday.value)
        
        added_hours = int(str(startHoursAdded.value)) * 60
        added_minutes = int(str(startMinutesAdded.value))
        
        duration_minutes = (added_hours + added_minutes)
        
        days = 0
        
        while duration_minutes > 0:
            minutes += 1

            if minutes > 59:
                hours += 1
                minutes = 0

                if clock_system == '12clock':
                    if hours == 12 and time_form == "pm":
                        time_form = "am"    

                    elif hours == 12 and time_form == "am":
                        time_form = "pm"

                    if hours == 12 and minutes == 0 and time_form == "am":
                        days += 1

                    if hours > 12:
                        hours = 1
                    
            if clock_system == '24clock':
                if hours == 24 and minutes == 0:
                    hours = 0
                    days += 1

            duration_minutes -= 1
            
        new_time += f"{0 if hours < 10 else ''}{hours}:{0 if minutes < 10 else ''}{minutes}{' '+time_form if time_form else ''}" 

        weekday_list = ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]

        if not week_day and days == 0:
            new_time += f", (same day)"
        
        if not week_day and days == 1:
            new_time += f" (next day)"

        if not week_day and days > 1:
            new_time += f" ({days} days later)"
        
        
        if week_day and days == 0:
            new_time += f", {week_day} (same day)"
        
        if week_day and days == 1:
            new_time += f", {weekday_list[(weekday_list.index(week_day.lower().capitalize()) + 1)]} (next day)"

        if week_day and days > 1:
            day = weekday_list.index(week_day.lower().capitalize())
            weekday_list = (weekday_list*int(((day + days + 1) / len(weekday_list)) + ((day + days + 1) % len(weekday_list) > 0)))
            new_time += f", {weekday_list[day + days]} ({days} days later)"
        
        outputDiv.textContent = new_time

def pressButtons(*args):   
    document.getElementById('clockSystem').onclick = lambda *args: showTimeFormDiv()
    document.getElementById('funcbutton').onclick = lambda *args: timefunc()
    
def onchange(*args):
    clockSystem.onchange = showTimeFormDiv
    timeForm.onchange = showTimeDiv
    
    
if __name__ == '__main__':
    
    clockSystem = document.getElementById('clockSystem')                # 12 or 24 element

    timeFormDiv = document.getElementById('timeFormDiv')                # AM or PM div
    timeStartDiv = document.getElementById('timeStartDiv')              # Start time div
    weekdayDiv = document.getElementById('weekdayDiv')                  # Weekdays div
    timeAddedDiv = document.getElementById('timeAddedDiv')              # Added time div
    
    timeForm = document.getElementById('timeForm')                      # AM or PM element
    startHours = document.getElementById('startHours')                  # Start time in hours element
    startMinutes = document.getElementById('startMinutes')              # Start time in minutes element
    weekday = document.getElementById('weekday')                        # Weekday element
    startHoursAdded = document.getElementById('startHoursAdded')        # Start time in hours with added hours element
    startMinutesAdded = document.getElementById('startMinutesAdded')    # Start time in minutes with added minutes element
    
    warningDiv = document.getElementById('warningDiv')                  # Warning div
    outputDiv = document.getElementById('outputDiv')                    # Output div
    
    onchange()
    
    pressButtons()
    
    if runFooter := True:
        document.getElementById('footer').textContent = f'© 2020 - {datetime.datetime.now().year} - sericakitty.github.io. All Rights Reserved.'
        runFooter = False
