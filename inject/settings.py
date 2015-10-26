import sys


ELASTIC_TIMEOUT = 10
ELASTIC_URI = 'localhost:9201'
MAG_PATH = '/Volumes/Seagate/MicrosoftAcademicGraph/'
ELASTIC_INDEX = "mag"
FIELD_NAMES = {
    'Affiliations': ('affiliation_id',
                     'affiliation_name'),
    'Authors': ('author_id',
                'author_name'),
    'ConferenceSeries': ('conference_series_id',
                         'short_name',
                         'full_name'),
    'ConferenceInstances': ('conference_series_id',
                            'conference_instance_id',
                            'short_name',
                            'full_name',
                            'location',
                            'official_conference_url',
                            'conference_start_date',
                            'conference_end_date',
                            'conference_abstract_registration_date',
                            'conference_submission_deadline_date',
                            'conference_notification_due_date',
                            'conference_final_version_due_date'),
    'FieldsOfStudy': ('field_of_study_id',
                      'field_of_study_name'),
    'Journals': ('journal_id',
                 'journal_name'),
    'Papers': ('paper_id',
               'original_paper_title',
               'normalized_paper_title',
               'paper_publish_year',
               'paper_publish_date',
               'paper_doi',
               'original_venue_name',
               'normalized_venue_name',
               'journal_id_mapped_to_venue_name',
               'conference_series_id_mapped_to_venue_name',
               'paper_rank'),
    'PaperAuthorAffiliations': ('paper_id',
                                'author_id',
                                'affiliation_id',
                                'original_affiliation_name',
                                'normalized_affiliation_name',
                                'author_sequence_number'),
    'PaperKeywords': ('paper_id',
                      'keyword_name',
                      'field_of_study_id_mapped_to_keyword'),
    'PaperReferences': ('paper_id',
                        'paper_reference_id'),
    'PaperUrls': ('paper_id',
                  'url')
}

TABLE_IDs = {
    'Affiliations': 1,
    'Authors': 1,
    'ConferenceSeries': 1,
    'ConferenceInstances': 2,
    'FieldsOfStudy': 1,
    'Journals': 1,
    'Papers': 1,
    'PaperAuthorAffiliations': 3,
    'PaperKeywords': 1,
    'PaperReferences': 2,
    'PaperUrls': 1
}

TYPES = {
    'Affiliations': 'affiliations',
    'Authors': 'authors',
    'ConferenceSeries': 'conference_series',
    'ConferenceInstances': 'conference_instances',
    'FieldsOfStudy': 'fields_of_study',
    'Journals': 'journals',
    'Papers': 'papers',
    'PaperAuthorAffiliations': 'paper_author_affiliations',
    'PaperKeywords': 'paper_keywords',
    'PaperReferences': 'paper_references',
    'PaperUrls': 'paper_urls'
}
