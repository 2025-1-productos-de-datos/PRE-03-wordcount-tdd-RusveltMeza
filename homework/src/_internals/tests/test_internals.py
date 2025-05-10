import subprocess
from ...wordcount import parse_arg



def test_parse_args():

    try:
        subprocess.run(
            ["python3", "-m", "homework", "data/input", "data/output"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")


    input_folder, output_folder = test_parse_args()
    assert input_folder=="input/"
    assert output_folder=="data/output/"
   