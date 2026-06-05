import typer
from typing import Optional

app = typer.Typer()


@app.command()
def first_cmd(cmd: Optional[str] = None):
    arguments = [
        {
            "flags": ["square"],
            "kwargs": {
                "type": int,
                "help": "display the square of a given number"
            }
        },
        {   "flags": ["names"],
            "kwargs": {
                "type": str,
                "help": "display the names(s) specified in the args"
            }
        },
        {
            "flags": ["-v", "--verbosity"],
            "kwargs": {
                "type": int,
                "help": "increase the output verbosity"
            }
        },
    ]
    
    # cmd -> command
        
        
    
    
    
    


if __name__ == "__main__":
    app()