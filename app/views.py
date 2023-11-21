from django.shortcuts import render
from .utils import grammar_check
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def dashboard(request):
    return render(request, "dashboard.html")


def grammar_spell_checker(request):
    data = dict()
    if request.method == "POST":
        sentence = request.POST["inputTextbox"]
        corrected_text = grammar_check(sentence)
        data["sentence"] = sentence
        data["corrected_text"] = corrected_text
    return render(
        request,
        "grammar_and_spell_checker.html",
        context={
            "previous_sent": data.get("sentence"),
            "new_sent": data.get("corrected_text"),
        },
    )


def paraphrasing(request):
    data = dict()
    if request.POST:
        text = request.POST["inputTextbox"]
        # Load pre-trained GPT-2 model and tokenizer
        model_name = "gpt2"
        text = request.POST["inputTextbox"]
        data["text"] = text
        model = GPT2LMHeadModel.from_pretrained(model_name)
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)

        # Tokenize input text
        input_ids = tokenizer.encode(text, return_tensors="pt")

        # Generate paraphrased text
        output = model.generate(
            input_ids,
            max_length=150,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.95,
        )

        # Decode the generated output
        paraphrased_text = tokenizer.decode(output[0], skip_special_tokens=True)
        # import pdb;pdb.set_trace()
        data["paraphrased_text"] = paraphrased_text
    return render(
        request,
        "paraphrasing.html",
        context={
            "previous_sent": data.get("text"),
            "new_sent": data.get("paraphrased_text"),
        },
    )
