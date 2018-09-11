#include <stdio.h>

#define SFID 0
#define FCC 1
#define NONE 2

struct fream_format
{
  int word_length;
  int sub_fream_length;
  int major_fream_length;
  int sub_fream_type;
  int sync_word_length;
  int sunc_word_position;
  int sfid_position;
  char *sync_word;
};

struct fream_format read_cfg(FILE *fp_cfg);
int adjuage_sfid(FILE *fp_data, struct fream_format fream);
int adjuage_fcc(FILE *fp_data, struct fream_format fream);
int adjuage_none(FILE *fp_data, struct fream_format fream);

int main()
{
  FILE *fp_cfg, *fp_data;
  struct fream_format fream;
  if ((fp_cfg = fopen("/home/walter/cfg.txt", "r")) != NULL)
    fream = read_cfg(*fp_cfg);
  else
    return 1;

  if (fream.sub_fream_type == 0)
    adjuage_sfid(*fp_data, fream);
  else if (fream.sub_fream_type == 1)
    adjuage_fcc(*fp_data, fream);
  else if (fream.sub_frea_type == 2)
    adjuage_none(*fp_data, fream);
  else
    return 1;

  if ((fclose(*fp_data)) == 0)
    return 0;
  else
    return 1;
  
}
