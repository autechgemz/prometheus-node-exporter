# Ansible Role: prometheus-node-exporter

## Description

Manage the prometheus exporter for machine metrics.

## Requirements

- Ansible 2.9 or higher

## Dependencies

None

## OS Platforms

- AlmaLinux 8 or higher
- RockyLinux 8 or higher
- Ubuntu 24.04 or higher

## Example Playbook

```yaml
- hosts: all
  roles:
    - prometheus-node-exporter
```

## Role Variables

### node_exporter_debug: (default: false)

```yaml
node_exporter_debug: false
```

### node_exporter_install_source: (default: 'package')

```yaml
node_exporter_install_source: 'package'
```

### node_exporter_install_prefix: (default: '/opt')

* This parameter is only applicable when `node_exporter_install_source` is set to `'binary'`.

```yaml
node_exporter_install_prefix: '/opt'
```

### node_exporter_install_url: (default: null)

* This parameter is only applicable when `node_exporter_install_source` is set to `'binary'`.

```yaml
node-exporter_install_url: null
```

### node_exporter_package_ensure: (default: present)

```yaml
node_exporter_package_ensure: present
```

### node_exporter_service_ensure: (default: 'started')

```yaml
node_exporter_service_ensure: 'started'
```

### node_exporter_service_enable: (default: true)

```yaml
node_exporter_service_enable: true
```

### node_exporter_daemon_config_options: (default: [])

```yaml
node_exporter_daemon_config_options: []
```

### node_exporter_systemd_options: (default: {})

```yaml
node_exporter_systemd_options: {}
```

## Handlers

The role includes the following handlers:

- `Restart node-exporter`: Restarts the node-exporter service.
- `Reload node-exporter`: Reloads the node-exporter service.

## Example vars

```yaml
node_exporter_install_source: 'binary'
```

## Example test

```yaml
ansible-playbook -i 192.168.56.101, playbook.yml -e ansible_user=vagrant

py.test -v --hosts=all --ansible-inventory=hosts --connection=ansible tests/test.py
```

## License

This role is under the MIT License. See the LICENSE file for the full license text.
