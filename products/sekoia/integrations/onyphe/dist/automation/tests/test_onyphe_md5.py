import pytest
from generic_onyphe_tests import *  # noqa: F401, F403

from onyphe.action_onyphe_md5 import OnypheMD5Action
from onyphe.errors import InvalidArgument


@pytest.fixture
def OnypheAction():
    return OnypheMD5Action


@pytest.fixture
def ressource():
    return "md5/7a1f20cae067b75a52bc024b83ee4667"


@pytest.fixture
def bad_ressource():
    return "md5/1234"


@pytest.fixture
def arguments():
    return {"md5": "7A1F20CAE067B75A52BC024B83EE4667"}


@pytest.fixture
def bad_arguments():
    return [
        (InvalidArgument, {"md5": 1234}),
        (InvalidArgument, {"md5": "1234"}),
        (TypeError, {}),
    ]


md5_result = {
    "count": 10,
    "error": 0,
    "max_page": 1,
    "myip": "185.122.161.248",
    "page": 1,
    "results": [
        {
            "@category": "datascan",
            "@timestamp": "2019-09-17T13:56:57.000Z",
            "@type": "doc",
            "seen_date": "2019-09-17",
            "source": "datascan",
            "ip": "221.227.75.193",
            "organization": "No.31,Jin-rong Street",
            "country": "CN",
            "asn": "AS4134",
            "city": "Wuxi",
            "data": "SSH-2.0-OpenSSH_7.4\\x0d\n",
            "datamd5": "7a1f20cae067b75a52bc024b83ee4667",
            "ipv6": "false",
            "location": "31.5689,120.2886",
            "port": "3389",
            "product": "OpenSSH",
            "productvendor": "OpenBSD",
            "productversion": "7.4",
            "protocol": "ssh",
            "protocolversion": "2.0",
            "subnet": "221.227.0.0/17",
            "tls": "false",
            "transport": "tcp",
        },
        {
            "@category": "datascan",
            "@timestamp": "2019-09-17T13:50:35.000Z",
            "@type": "doc",
            "seen_date": "2019-09-17",
            "source": "datascan",
            "ip": "129.232.188.197",
            "country": "ZA",
            "organization": "HETZNER",
            "asn": "AS37153",
            "data": "SSH-2.0-OpenSSH_7.4\\x0d\n",
            "datamd5": "7a1f20cae067b75a52bc024b83ee4667",
            "ipv6": "false",
            "location": "-29.0000,24.0000",
            "port": "5432",
            "product": "OpenSSH",
            "productvendor": "OpenBSD",
            "productversion": "7.4",
            "protocol": "ssh",
            "protocolversion": "2.0",
            "subnet": "129.232.176.0/20",
            "tls": "false",
            "transport": "tcp",
        },
        {
            "@category": "datascan",
            "@timestamp": "2019-09-17T13:50:09.000Z",
            "@type": "doc",
            "seen_date": "2019-09-17",
            "source": "datascan",
            "ip": "117.94.180.159",
            "country": "CN",
            "organization": "No.31,Jin-rong Street",
            "asn": "AS4134",
            "city": "Taizhou",
            "data": "SSH-2.0-OpenSSH_7.4\\x0d\n",
            "datamd5": "7a1f20cae067b75a52bc024b83ee4667",
            "ipv6": "false",
            "location": "32.4907,119.9081",
            "port": "3389",
            "product": "OpenSSH",
            "productvendor": "OpenBSD",
            "productversion": "7.4",
            "protocol": "ssh",
            "protocolversion": "2.0",
            "subnet": "117.94.128.0/18",
            "tls": "false",
            "transport": "tcp",
        },
        {
            "@category": "datascan",
            "@timestamp": "2019-09-17T13:47:23.000Z",
            "@type": "doc",
            "country": "JP",
            "domain": "cnode.io",
            "hostname": ["v118-27-16-177.985k.static.cnode.io"],
            "ip": "118.27.16.177",
            "organization": "GMO Internet,Inc",
            "seen_date": "2019-09-17",
            "source": "datascan",
            "tld": "io",
            "host": "v118-27-16-177",
            "asn": "AS7506",
            "city": "Shibuya",
            "data": "SSH-2.0-OpenSSH_7.4\\x0d\n",
            "datamd5": "7a1f20cae067b75a52bc024b83ee4667",
            "ipv6": "false",
            "location": "35.6624,139.7036",
            "port": "21",
            "product": "OpenSSH",
            "productvendor": "OpenBSD",
            "productversion": "7.4",
            "protocol": "ssh",
            "protocolversion": "2.0",
            "reverse": "v118-27-16-177.985k.static.cnode.io",
            "subdomains": ["static.cnode.io", "985k.static.cnode.io"],
            "subnet": "118.27.0.0/17",
            "tls": "false",
            "transport": "tcp",
        },
        {
            "@category": "datascan",
            "@timestamp": "2019-09-17T13:38:38.000Z",
            "@type": "doc",
            "country": "US",
            "domain": "mediamaster.us",
            "hostname": ["rtun.mediamaster.us"],
            "ip": "138.197.93.140",
            "organization": "DigitalOcean, LLC",
            "seen_date": "2019-09-17",
            "source": "datascan",
            "tld": "us",
            "host": "rtun",
            "asn": "AS14061",
            "city": "Clifton",
            "data": "SSH-2.0-OpenSSH_7.4\\x0d\n",
            "datamd5": "7a1f20cae067b75a52bc024b83ee4667",
            "ipv6": "false",
            "location": "40.8364,-74.1403",
            "port": "110",
            "product": "OpenSSH",
            "productvendor": "OpenBSD",
            "productversion": "7.4",
            "protocol": "ssh",
            "protocolversion": "2.0",
            "reverse": "rtun.mediamaster.us",
            "subnet": "138.197.0.0/17",
            "tls": "false",
            "transport": "tcp",
        },
        {
            "@category": "datascan",
            "@timestamp": "2019-09-17T13:17:51.000Z",
            "@type": "doc",
            "country": "JP",
            "domain": "amazonaws.com",
            "hostname": ["ec2-52-193-147-147.ap-northeast-1.compute.amazonaws.com"],
            "ip": "52.193.147.147",
            "organization": "Amazon.com, Inc.",
            "seen_date": "2019-09-17",
            "source": "datascan",
            "host": "ec2-52-193-147-147",
            "tld": "com",
            "asn": "AS16509",
            "city": "Tokyo",
            "data": "SSH-2.0-OpenSSH_7.4\\x0d\n",
            "datamd5": "7a1f20cae067b75a52bc024b83ee4667",
            "ipv6": "false",
            "location": "35.6882,139.7532",
            "port": "22",
            "product": "OpenSSH",
            "productvendor": "OpenBSD",
            "productversion": "7.4",
            "protocol": "ssh",
            "protocolversion": "2.0",
            "reverse": "ec2-52-193-147-147.ap-northeast-1.compute.amazonaws.com",
            "subdomains": [
                "ap-northeast-1.compute.amazonaws.com",
                "compute.amazonaws.com",
            ],
            "subnet": "52.192.0.0/14",
            "tls": "false",
            "transport": "tcp",
        },
        {
            "@category": "datascan",
            "@timestamp": "2019-09-17T13:17:51.000Z",
            "@type": "doc",
            "country": "CN",
            "ip": "49.235.183.141",
            "organization": "Shenzhen Tencent Computer Systems Company Limited",
            "seen_date": "2019-09-17",
            "source": "datascan",
            "asn": "AS45090",
            "city": "Beijing",
            "data": "SSH-2.0-OpenSSH_7.4\\x0d\n",
            "datamd5": "7a1f20cae067b75a52bc024b83ee4667",
            "ipv6": "false",
            "location": "39.9288,116.3889",
            "port": "22",
            "product": "OpenSSH",
            "productvendor": "OpenBSD",
            "productversion": "7.4",
            "protocol": "ssh",
            "protocolversion": "2.0",
            "subnet": "49.232.0.0/14",
            "tls": "false",
            "transport": "tcp",
        },
        {
            "@category": "datascan",
            "@timestamp": "2019-09-17T13:17:51.000Z",
            "@type": "doc",
            "country": "CN",
            "ip": "188.131.232.31",
            "organization": "Shenzhen Tencent Computer Systems Company Limited",
            "seen_date": "2019-09-17",
            "source": "datascan",
            "asn": "AS45090",
            "data": "SSH-2.0-OpenSSH_7.4\\x0d\n",
            "datamd5": "7a1f20cae067b75a52bc024b83ee4667",
            "ipv6": "false",
            "location": "39.9289,116.3883",
            "port": "22",
            "product": "OpenSSH",
            "productvendor": "OpenBSD",
            "productversion": "7.4",
            "protocol": "ssh",
            "protocolversion": "2.0",
            "subnet": "188.131.128.0/17",
            "tls": "false",
            "transport": "tcp",
        },
        {
            "@category": "datascan",
            "@timestamp": "2019-09-17T13:17:51.000Z",
            "@type": "doc",
            "country": "AU",
            "domain": "amazonaws.com",
            "hostname": ["ec2-52-63-104-216.ap-southeast-2.compute.amazonaws.com"],
            "ip": "52.63.104.216",
            "organization": "Amazon.com, Inc.",
            "seen_date": "2019-09-17",
            "source": "datascan",
            "tld": "com",
            "host": "ec2-52-63-104-216",
            "subdomains": [
                "ap-southeast-2.compute.amazonaws.com",
                "compute.amazonaws.com",
            ],
            "asn": "AS16509",
            "city": "Sydney",
            "data": "SSH-2.0-OpenSSH_7.4\\x0d\n",
            "datamd5": "7a1f20cae067b75a52bc024b83ee4667",
            "ipv6": "false",
            "location": "-33.8591,151.2002",
            "port": "22",
            "product": "OpenSSH",
            "productvendor": "OpenBSD",
            "productversion": "7.4",
            "protocol": "ssh",
            "protocolversion": "2.0",
            "reverse": "ec2-52-63-104-216.ap-southeast-2.compute.amazonaws.com",
            "subnet": "52.62.0.0/15",
            "tls": "false",
            "transport": "tcp",
        },
        {
            "@category": "datascan",
            "@timestamp": "2019-09-17T13:17:51.000Z",
            "@type": "doc",
            "country": "CN",
            "domain": "hwclouds-dns.com",
            "hostname": ["ecs-114-115-232-179.compute.hwclouds-dns.com"],
            "ip": "114.115.232.179",
            "organization": "China Unicom Beijing Province Network",
            "seen_date": "2019-09-17",
            "source": "datascan",
            "tld": "com",
            "host": "ecs-114-115-232-179",
            "asn": "AS4808",
            "city": "Shenzhen",
            "data": "SSH-2.0-OpenSSH_7.4\\x0d\n",
            "datamd5": "7a1f20cae067b75a52bc024b83ee4667",
            "ipv6": "false",
            "location": "22.5333,114.1333",
            "port": "22",
            "product": "OpenSSH",
            "productvendor": "OpenBSD",
            "productversion": "7.4",
            "protocol": "ssh",
            "protocolversion": "2.0",
            "reverse": "ecs-114-115-232-179.compute.hwclouds-dns.com",
            "subdomains": "compute.hwclouds-dns.com",
            "subnet": "114.115.128.0/17",
            "tls": "false",
            "transport": "tcp",
        },
    ],
    "status": "ok",
    "took": "0.350",
    "total": 2532968,
}


@pytest.fixture
def result():
    return md5_result


@pytest.fixture
def result_page_0():
    return md5_result


@pytest.fixture
def result_page_1():
    return {}
