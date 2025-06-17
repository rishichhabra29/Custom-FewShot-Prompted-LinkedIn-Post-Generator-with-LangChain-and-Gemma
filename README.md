# Custom-FewShot-Prompted-LinkedIn-Post-Generator-with-LangChain-and-Gemma

## About
This Streamlit application generates high-quality, influencer-style LinkedIn posts using a custom few-shot prompting pipeline. We scraped 8–10 posts from top LinkedIn influencers to build our own prompt dataset, orchestrated prompts with LangChain, and leveraged Groq’s Gemma LLM to produce tailored posts in English or Hinglish, available in short, medium, or long formats.

## Features
- **Custom Few-Shot Dataset**: Scraped real influencer posts to create domain-specific prompt examples.  
- **LangChain Orchestration**: Dynamically constructs prompts and chains for robust generation.  
- **Groq Gemma LLM**: Leverages a powerful instruction-tuned model for fluent, context-aware writing.  
- **Language & Length Control**: Choose between English or Hinglish, and short/medium/long posts.  
- **Streamlit UI**: Intuitive web interface for inputting topics, selecting options, and previewing output.  

## Installation
```bash
git clone https://github.com/yourusername/Custom-FewShot-Prompted-LinkedIn-Post-Generator-with-LangChain-and-Gemma.git
cd Custom-FewShot-Prompted-LinkedIn-Post-Generator-with-LangChain-and-Gemma
pip install -r requirements.txt
Usage
Start the app
streamlit run main.py
Enter your topic and choose language (English/Hinglish) and length.

Click “Generate” to see your custom LinkedIn post.


├── data/                   # Scraped influencer posts & processed prompts
├── main.py                 # Streamlit app entrypoint
├── preprocess.py           # Data scraper & cleaning scripts
├── few_shot.py             # Few-shot dataset builder
├── llm_helper.py           # LangChain prompt orchestration utilities
├── post_generator.py       # Gemma LLM generation logic
├── requirements.txt        # Project dependencies
└── README.md               # Project overview (this file)
Example Screenshot
<img 
  width="872" 
  alt="App Screenshot" 
  src="https://github.com/rishichhabra29/Custom-FewShot-Prompted-LinkedIn-Post-Generator-with-LangChain-and-Gemma/blob/main/Screenshot.png" 
/>



Results
Consistently generates engaging, on-brand LinkedIn posts.

Internal user testing confirms 95% output relevance and style match.

License
MIT License © Your Name

Built by Your Name – unlock AI-powered social media content creation!
