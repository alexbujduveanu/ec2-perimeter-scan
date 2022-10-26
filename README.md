# EC2-Perimeter-Scan
Automation to sweep over EC2 inventory, feed results programmatically to nmap, and then post results to Slack

# Summary
In modern cloud environments I have personally encountered several different ways in which firewall rules can be set. Some examples are:
- Using cloud primitives like AWS security groups
- Using Linux command line tools like `iptables`
- Using containerization concepts like network plugins, K8s manifests, etc.

If used in parallel, these can over-ride each other depending on which rules are more specific. This is a common trend I see in SaaS startups that have their infrastructure and tools sprawl as they go through hypergrowth. Hence, the approach here is just to scan these machines from a complete outsider's point of view - this will produce a list of the highest priority attack surface by virtue of the fact that anything in these reports will be proved as being directly internet-facing.
