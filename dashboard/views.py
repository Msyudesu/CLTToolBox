from django.shortcuts import render

apps = [
    {
        'title'          : 'Daily Output Log',
        'description'    : 'For self-reporting column loading totals and daily shift comments or issues.',
        'url'            : "cltlog-home",
        'request_path'   : "/cltlog/",
        'icon'           : 'fa fa-database'
    },
    {
        'title'         : 'FTO Calendar',
        'description'   : 'Schedule time off here!',
        'url'           : 'dashboard-home',
        'request_path'  : "/#/",
        'icon'          : 'fa fa-calendar'
    },
    {
        'title'         : 'Overtime Sign Up',
        'description'   : 'Schedule your overtime here!',
        'url'           : 'dashboard-home',
        'request_path'  : "/#/",
        'icon'          : 'fa fa-calendar-check-o'
    },
    {
        'title'         : 'Issue Reporting',
        'description'   : 'Report general production related issues encountered during your shift.',
        'url'           : 'dashboard-home',
        'request_path'  : "/#/",
        'icon'          : 'fa fa-exclamation-triangle'
    }
]
def home(request):
    context = {
        'title' :   'Dashboard Home',
        'apps'  :   apps
    }
    return render(request, 'dashboard/home.html', context)