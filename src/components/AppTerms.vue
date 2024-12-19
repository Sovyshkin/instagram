<script>
export default {
  name: "AppTerms",
  components: {},
};
</script>
<template>
  <div class="wrapper">
    <div class="wrap-info">
      <h1>Terms and Conditions Last Updated: 01 December 2024</h1>
      <span class="desc"
        >Welcome to IGShift (“Service”, “we”, “our”, “us”). These Terms and
        Conditions govern your use of our platform, which allows you to transfer
        Instagram bookmarks and connections (friends) from one account to
        another. By using the Service, you agree to these Terms.</span
      >
      <div class="info">
        <div class="group">
          <h2>1. Acceptance of Terms</h2>
          <span
            >By accessing or using the Service, you confirm that you have read,
            understood, and agree to be bound by these Terms and our Privacy
            Policy. If you do not agree, you may not use the Service.</span
          >
        </div>
        <div class="group">
          <h2>2. Services Provided</h2>
          <span
            >We facilitate the migration of data (such as bookmarks and friend
            lists) between Instagram accounts. This process requires temporary
            access to the credentials and content of your Instagram
            accounts.</span
          >
        </div>
        <div class="group">
          <h2>3. Account and Access Permissions</h2>
          <span class="text-list">To provide the Service:</span>
          <span
            >1. Login Credentials: You agree to grant us access to your
            Instagram account(s), including usernames and passwords.</span
          >
          <span
            >2. Account Content: You permit us to access account-related data,
            including bookmarks, connections (friends), and account-related
            content necessary for the transfer.</span
          >
          <span
            >3. Scope of Access: Access is temporary and used exclusively for
            data migration purposes. Credentials are processed securely and not
            stored beyond the required period.</span
          >
          <span
            >4. User Authorization: You confirm you are the legitimate owner of
            the accounts involved and authorize such access.</span
          >
        </div>
        <div class="group">
          <h2>4. Personal Data and Privacy</h2>
          <span
            >We value your privacy. By using our Service, you consent to the
            collection and use of your personal data as described here:</span
          >
          <span
            >Data Collected: Login credentials, bookmarks, friends list, and
            other content required for the migration.</span
          >
          <span
            >Use of Data: Data is accessed strictly for the purpose of executing
            the account migration.</span
          >
          <span
            >Storage and Deletion: Personal data, including passwords, are not
            stored permanently. Once the migration is complete, data is securely
            deleted.</span
          >
          <span
            >Third-Party Platforms: We are not affiliated with Instagram or Meta
            Platforms, Inc. By using the Service, you understand that
            Instagram’s terms and policies still apply to your accounts.</span
          >
        </div>
        <div class="group">
          <h2>5. User Responsibilities</h2>
          <span class="text-list">You agree to: </span>
          <span>1. Provide accurate and truthful account information.</span>
          <span
            >2. Ensure that you have the right to access and transfer the data
            in your account(s).</span
          >
          <span
            >3. Use the Service for lawful purposes and comply with Instagram’s
            Terms of Service.</span
          >
          <span
            >4. Safeguard your accounts after migration (e.g., updating your
            password if required).</span
          >
        </div>
        <div class="group">
          <h2>6. Service Limitations and Risks</h2>
          <span class="text-list">You acknowledge that: </span>
          <span>We cannot guarantee uninterrupted access to the Service.</span>
          <span
            >There may be risks associated with providing account credentials.
            While we use industry-standard security practices, unauthorized
            access or account suspension by Instagram cannot be ruled out.</span
          >
          <span
            >We are not liable for any changes to your accounts resulting from
            Instagram’s monitoring, policies, or security measures.</span
          >
        </div>
        <div class="group">
          <h2>7. Security Measures</h2>
          <span
            >We implement advanced security protocols to safeguard your data.
            However, you acknowledge that no method of transmission over the
            internet or electronic storage is 100% secure.</span
          >
        </div>
        <div class="group">
          <h2>8. Disclaimers</h2>
          <span>The Service is provided on an “as-is” basis. </span>
          <span
            >We make no warranties regarding the accuracy, completeness, or
            functionality of the Service.</span
          >
          <span
            >We are not liable for any direct, indirect, or incidental damages
            resulting from your use of the Service.</span
          >
        </div>
        <div class="group">
          <h2>9. Termination</h2>
          <span
            >We reserve the right to suspend or terminate your access to the
            Service at any time for violations of these Terms or misuse of the
            Service.</span
          >
        </div>
        <div class="group">
          <h2>10. Indemnification</h2>
          <span
            >You agree to indemnify and hold harmless
            <a href="https://igshift.me/" target="_blank">IGShift.me</a> and its
            affiliates from any claims, liabilities, or damages arising from
            your use of the Service, including unauthorized account
            activity.</span
          >
        </div>
        <div class="group">
          <h2>11. Changes to Terms</h2>
          <span
            >We may update these Terms from time to time. You will be notified
            of significant changes, and your continued use of the Service
            constitutes acceptance of the updated Terms.</span
          >
        </div>
        <div class="group">
          <h2>12. Contact Us</h2>
          <span
            >For questions or concerns regarding these Terms or the Service,
            contact us at: <a href="ask@igshift.com">ask@igshift.com</a>.
          </span>
          <span>---</span>
          <span
            >By clicking “Accept” or using the Service, you confirm that you
            have read, understood, and agreed to these Terms and
            Conditions</span
          >
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
  border-radius: 20px;
  padding: 30px;
  gap: 30px;
  background-color: #1f1f1f;
}

.wrap-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
  gap: 30px;
  width: 100%;
  max-width: 900px;
}

.info {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

h1 {
  font-weight: 400;
  font-size: 16px;
  line-height: 20px;
  text-align: center;
}

h2 {
  font-weight: 400;
  line-height: 20px;
  font-size: 16px;
}

.desc {
  font-weight: 400;
  line-height: 19px;
  font-size: 14px;
  text-align: center;
  opacity: 60%;
}

span {
  font-weight: 400;
  line-height: 19px;
  font-size: 14px;
  opacity: 60%;
}

span a {
  color: rgb(14, 14, 242);
}

.text-list {
  opacity: 80%;
}
</style>
