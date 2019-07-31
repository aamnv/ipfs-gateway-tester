import requests
import time, csv


hashes = [
    'QmSQfLsPDKaFJM3SPKZYU971XSCArXKVCAWcEzQaKgtxQp', # file_hash 1.3KB
    'QmUTcaZg3UVqKxM8GvjEVjtNaFDCsG3EAQAU4nzmdi7Vis', # image_hash 3.6MB
    'QmbvdTQ5eCS7MqBfqv93Pdhy74p95XHuLh5nzSmaQiu6wk' #video_hash 153.3MB
]

gateway_providers = [
    {
        'provider': 'Protocol Labs',
        'gateway_url': 'https://ipfs.io/ipfs/'
    },
    {
        'provider': 'Cloudflare',
        'gateway_url': 'https://cloudflare-ipfs.com/ipfs/'
    },
    {
        'provider': 'Infura',
        'gateway_url': 'https://ipfs.infura.io/ipfs/'
    },
    {
        'provider': 'Pinata',
        'gateway_url': 'https://gateway.pinata.cloud/ipfs/'
    },
    {
        'provider': 'Eternum',
        'gateway_url': 'https://ipfs.eternum.io/ipfs/'
    },
    {
        'provider': 'Siderus',
        'gateway_url': 'https://siderus.io/ipfs/'
    },
    {
        'provider': 'Temporal',
        'gateway_url': 'https://gateway.temporal.cloud/ipfs/'
    }
]


def test_url(url):

    start = time.time()
    r = requests.get(url)
    end = time.time()

    time_elapsed = end - start
    time_in_ms = time_elapsed * 1000

    return time_in_ms


with open('results.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['provider', 'hash', 'time (ms)'])

    for provider_entry in gateway_providers:
        base_url = provider_entry['gateway_url']

        for hash in hashes:
            call_url = base_url + hash

            for i in range(10):
                result = test_url(call_url)
                writer.writerow([provider_entry['provider'], hash, result])
                time.sleep(1)

                print(f'Finished attempt {i} on hash: {hash}')
