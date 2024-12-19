# import laion_clap
# import os
# from torch.nn.functional import cosine_similarity

# model = laion_clap.CLAP_Module(enable_fusion=False)
# model.load_ckpt()


# audio_org_emd = model.get_audio_embedding_from_filelist([audio_file_org], use_tensor=True)
# audio_bad_emd = model.get_audio_embedding_from_filelist([audio_file_bad], use_tensor=True)
# audio_3_emd = model.get_audio_embedding_from_filelist([audio_file_3], use_tensor=True)
# audio_os_emd = model.get_audio_embedding_from_filelist([audio_file_os], use_tensor=True)
# text_emd = model.get_text_embedding(text, use_tensor=True)

# print(f"Org sim: {cosine_similarity(text_emd, audio_org_emd).item()}")
# print(f"Bad sim: {cosine_similarity(text_emd, audio_bad_emd).item()}")
# print(f"3 sim: {cosine_similarity(text_emd, audio_3_emd).item()}")
# print(f"Os sim: {cosine_similarity(text_emd, audio_os_emd).item()}")