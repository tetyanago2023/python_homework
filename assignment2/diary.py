# diary.py

#Task 1
import traceback


def write_to_diary():
    try:
        with open("diary.txt", "a") as diary:
            prompt = "What happened today? "
            while True:
                try:
                    entry = input(prompt)
                except EOFError:
                    print("\nEOFError: Detected EOF (Ctrl-D). Exiting gracefully.")
                    break
                except KeyboardInterrupt:
                    print("\nKeyboardInterrupt: User interrupted (Ctrl-C). Exiting gracefully.")
                    break

                diary.write(entry + "\n")
                if entry.lower() == "done for now":
                    break
                prompt = "What else? "
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [
            f'File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}'
            for trace in trace_back
        ]
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


if __name__ == "__main__":
    write_to_diary()
