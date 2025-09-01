import pandas as pd

def read_dataframe(file_path, max_rows=5):
    """
    Reads a CSV file into a Pandas DataFrame and returns a preview as a string.
    The preview is limited to max_rows to avoid overwhelming the model.
    """
    try:
        # Try utf-8 first, fall back to latin1 if it fails
        try:
            df = pd.read_csv(file_path, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding="latin1")

        preview = df.head(max_rows).to_string(index=False)
        info = (
            f"DataFrame loaded from {file_path} "
            f"with {len(df)} rows and {len(df.columns)} columns.\nPreview:\n{preview}"
        )
        return info
    except Exception as e:
        return f"Error reading dataframe: {str(e)}"
