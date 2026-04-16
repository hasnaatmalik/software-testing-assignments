# Assignment 04 - Node.js Authentication App, Test Automation & CI/CD

**Author:** Muhammad Hasnaat Raza  
**Submission Date:** April 2026  

## 📖 Project Overview
This repository contains a full-stack Node.js authentication system featuring custom User Registration (Signup) and Authentication (Login) logic. The project is tightly evaluated against an industrial testing methodology using the **Page Object Model (POM)** pattern.

### Testing Purpose
The core objective of automation in this system is to prevent regressions regarding security and validation boundaries. By mimicking actual user behavior through Selenium and systematically tracking constraints (username lengths, invalid emails) via Mocha unit tests, the development cycle guarantees robust authentication deployments securely tracked via a Jenkins CI/CD pipeline.

## 🛠️ Tech Stack
- **Node.js** & **Express** -> Core Backend Server
- **Mocha** & **Chai** -> Testing Framework and Assertion Library
- **Selenium WebDriver** -> UI / Browser Interaction
- **Jenkins** -> CI/CD Pipeline Automation

---

## 📊 Test Summary Table

| Type | Count | Status |
| :--- | :---: | :---: |
| **Unit Tests** | 8 | ✅ PASS |
| **Integration Tests** | 10+ | ✅ PASS |
| **Total Tests** | 18+ | ✅ PASS |

---

## ⚙️ Jenkins Pipeline Explanation
A declarative Pipeline (`Jenkinsfile`) is provided. It consists of the following stage-wise breakdown:

1. **Checkout Code:** Pulls the repository contents.
2. **Install Dependencies:** Executes `npm install`.
3. **Run Unit Tests:** Triggers the decoupled, stateless validation rules via `npm run test:unit`.
4. **Run Integration Tests:** Spins up the server concurrently (`npm start &`) and executes the heavy-duty UI selenium processes, verifying end-to-end functionality.
5. **Generate Reports:** Captures the `mochawesome` HTML outputs and archives them automatically to your Jenkins artifacts.

---

## 🏃 Local Execution Guidelines

1. Install project and reporting dependencies:
   ```bash
   npm install
   npm install --save-dev mochawesome
   ```

2. **Boot the App:**
   ```bash
   npm start
   ```

3. **Run the Suites (in another terminal):**
   ```bash
   npm run test:unit
   npm run test:integration
   ```

4. View the generated `mochawesome-report/mochawesome.html` in your browser!
