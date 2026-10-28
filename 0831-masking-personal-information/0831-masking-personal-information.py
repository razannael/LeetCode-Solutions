class Solution:
    def maskPII(self, s: str) -> str:
        def email_mask(s):
            name, domain = s.split('@')
            name, domain = name.lower(), domain.lower()
            return name[0] + "*****" + name[-1] + "@" + domain

        def phone_mask(s):
            plan = s
            for ch in ['+', '-', '(', ')', ' ']:
                plan = plan.replace(ch, '')

            country_len = len(plan) - 10
            local = plan[-4:]

            if country_len == 0:
                return "***-***-" + local
            return "+" + "*" * country_len + "-***-***-" + local

        if '@' in s:
            return email_mask(s)
        return phone_mask(s)