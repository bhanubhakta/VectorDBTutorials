import imageio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def capture_svg_frames(svg_file_path, output_dir, frame_count, delay):
    # Setup Chrome options
    options = Options()
    options.headless = True  # Run in headless mode
    # Specify the path to ChromeDriver
    service = Service(executable_path='./chromedriver')

    # Create a new instance of Chrome
    with webdriver.Chrome(service=service, options=options) as driver:
        driver.get(svg_file_path)  # Load the SVG URL or local file
        for i in range(frame_count):
            screenshot_path = f"{output_dir}/frame_{i}.png"
            driver.save_screenshot(screenshot_path)
            time.sleep(delay)  # Wait for the specified delay


# Configure your parameters
svg_file_path = 'file:///Users/bhanusigdel/workspace/LeetCodeVideos/RAG.svg'
output_dir = './frames'
frame_count = 600
delay = 0.01  # Delay in seconds

# capture_svg_frames(svg_file_path, output_dir, frame_count, delay)


def create_gif_from_frames(frames_folder, output_gif, duration=0.01):
    images = [imageio.imread(f"{frames_folder}/frame_{i}.png")
              # Use the same frame_count
              for i in range(frame_count - 1, -1, -1)]
    imageio.mimsave(output_gif, images, duration=duration, loop=0)


create_gif_from_frames('./frames', 'output.gif', duration=0.01)
