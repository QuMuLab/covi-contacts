from . external import contact_matrices

__all__ = ['main']

def main(country=None, region=None):
    contact_matrices.main(country, region)