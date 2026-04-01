def save_as_bed(islands, filename, chrom="chr22"):
    """
    Converts a list of coordinate tuples into a standard 3-column BED file.

    Args:
        islands (list): List of (start, end) tuples.
        filename (str): Path to the output .bed file.
        chrom (str): Chromosome name (default "chr22").
    """
    try:
        with open(filename, 'w') as f:
            for start, end in islands:
                # BED format is: Chromosome [tab] Start [tab] End
                f.write(f"{chrom}\t{start}\t{end}\n")
        print(f"Successfully generated BED file: {filename}")
    except Exception as e:
        print(f"Error saving BED file: {e}")