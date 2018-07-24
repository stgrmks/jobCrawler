# StepStone config
StepStone_config = {
    'job_title': 'data+science',
    'location': 'Ingolstadt',
    'radius': 100,
    'jobs_per_page': 100,
    'startPage': 0,
    'maxPages': 10,
}
StepStone_config['url'] = 'https://www.stepstone.de/5/ergebnisliste.html?ke={}&ws={}&ra={}&li={}&suid=2c0c263d-efde-4d1c-92e1-5915c934b60c'.format(StepStone_config['job_title'], \
                                                                                                      StepStone_config['location'], StepStone_config['radius'], StepStone_config['jobs_per_page'])

# Monster config