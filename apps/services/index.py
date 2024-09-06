import dns.resolver

def get_domain_ip(domain: str=None, rdtype: str="A", nameservers=None):
    myResolver = dns.resolver.Resolver()

    if nameservers is not None:
        myResolver.nameservers = nameservers
    
    query_object = myResolver.resolve(qname=domain, rdtype=rdtype)

    return query_object
