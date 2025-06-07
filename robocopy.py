import os
import subprocess

class Robocopier:
    def __init__(self, src_uri: str, dest_uri: str, threads: int = 12,
                 max_retries:int = 3, wait_time: int = 5):
        self.src_uri = src_uri
        self.dest_uri = dest_uri

        self.threads = threads
        self.max_retries = max_retries
        self.wait_time = wait_time

        self.run()
        return

    def run(self):
        command = ["robocopy", f'"{self.src_uri}"', f'"{self.dest_uri}"', "/E",
                   f"/MT:{self.threads}", "/COPY:DAT", f"/R:{self.max_retries}",
                   f"/W:{self.wait_time}", "/NFL", "/NDL"]

        with subprocess.Popen(" ".join(command), stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, text=True) as proc:
            for line in proc.stdout:
                print(line, end="") 

        return

def main():
    abs_src_uri = input("Enter the absolute source uri: ")
    abs_dest_uri = input("Enter the absolute destination uri: ")
    copier = Robocopier(abs_src_uri, abs_dest_uri)

    print("Execution complete.")
    return

if __name__ == "__main__":
    main()
