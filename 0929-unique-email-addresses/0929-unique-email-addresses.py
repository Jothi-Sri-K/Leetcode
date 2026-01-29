class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq_emails=set()
        for email in emails:
            local,domain=email.split('@')
            if '+' in local:
                local=local.split('+')[0]
            local=local.replace('.','')
            cleaned_email=local+'@'+domain
            uniq_emails.add(cleaned_email)
        return len(uniq_emails)
            
        