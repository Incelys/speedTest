import speedtest

def run_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps

    # Return the average of download and upload speeds
    return (download_speed + upload_speed) / 2