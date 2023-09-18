import gui
import test_speed

def main():
    # Create GUI window
    window = gui.Window("Network Speed Test", "pink")

    # Run network speed test
    result = test_speed.run_test()

    # Set result text color based on speed
    if result < 10:
        window.set_result_text_color("red")
    elif result < 50:
        window.set_result_text_color("blue")
    else:
        window.set_result_text_color("green")

    # Display result on GUI
    window.set_result_text(f"Upload/Download Speed: {result} Mbps")

    # Start GUI event loop
    window.run()

if __name__ == "__main__":
    main()
