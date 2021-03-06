from . external import contact_matrices
from . external import contact_duration_matrices

__all__ = ['mixing', 'duration']

def mixing(country=None, region=None):
    return contact_matrices.main(country, region)

def duration(country=None, seconds_per_minute=None):
    return contact_duration_matrices.main(country, seconds_per_minute)