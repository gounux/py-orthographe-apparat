import typer

from pyoa.core import encode_orthographe_d_apparat

app = typer.Typer()

@app.command()
def transcript_orthographe_apparat(text: str):
    oa = encode_orthographe_d_apparat(text)
    print(f"Orthographe d'apparat de '{text}' :")
    print(oa)

def main():
    app()
