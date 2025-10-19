
def test_system_type(host):
    assert host.system_info.type == "linux"

def test_system_dist(host):
    assert host.system_info.distribution in ["redhat", "centos", "almalinux", "rocky"]
    assert host.system_info.arch == 'x86_64'

def test_user(host):
    assert host.user("prometheus").exists

def package_candidates(host):
    d = host.system_info.distribution.lower()
    # common package name variants across distros
    if d in ("redhat", "centos", "rocky", "almalinux", "fedora"):
        return [
            "golang-github-prometheus-node-exporter",
            "prometheus-node-exporter",
            "node-exporter"
        ]
    return [
        "prometheus-node-exporter",
        "node-exporter",
        "golang-github-prometheus-node-exporter"
    ]

def is_installed_any(host, names):
    return any(host.package(n).is_installed for n in names)

def test_prometheus_pkg_installed(host):
    assert is_installed_any(host, package_candidates(host)), \
        "Prometheus package not installed for this distro"

def test_prometheusd_running_and_enabled(host):
    prometheusd = host.service("prometheus-node-exporter")
    assert prometheusd.is_running
    assert prometheusd.is_enabled

def test_prometheusd_socket(host):
    prometheusd_v4 = host.socket("tcp://9100")
    prometheusd_v6 = host.socket("tcp://:::9100")
    assert prometheusd_v4.is_listening
    assert prometheusd_v6.is_listening

