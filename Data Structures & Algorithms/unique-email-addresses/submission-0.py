class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique_emails = set()

        for email in emails:
            local, domain = email.split("@")

            # Ignore everything after '+'
            if "+" in local:
                local = local.split("+")[0]

            # Remove all '.'
            local = local.replace(".", "")

            # Add the actual email
            unique_emails.add(local + "@" + domain)

        return len(unique_emails)