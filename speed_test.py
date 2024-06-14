import speedtest

def test_speed():
    try:
        print("Creating Speedtest object...")
        st = speedtest.Speedtest()
        print("Starting download test...")
        st.download()
        print("Starting upload test...")
        st.upload()
        print("Sharing results...")
        st.results.share()

        results = st.results.dict()
        return {
            'download': results['download'] / 1_000_000,  # Convert to Mbps
            'upload': results['upload'] / 1_000_000,      # Convert to Mbps
            'ping': results['ping'],                      # Ping in ms
            'server': results['server']['name'],
            'timestamp': results['timestamp']
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
