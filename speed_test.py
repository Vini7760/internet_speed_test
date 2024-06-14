import speedtest

def test_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    st.results.share()

    results = st.results.dict()
    return {
        'download': results['download'] / 1_000_000,  # Convert to Mbps
        'upload': results['upload'] / 1_000_000,      # Convert to Mbps
        'ping': results['ping'],                      # Ping in ms
        'server': results['server']['name'],
        'timestamp': results['timestamp']
    }
